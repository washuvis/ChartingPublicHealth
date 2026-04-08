
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, fcluster


# ====== LOAD DATA & UPDATING FEATURE NAMES
csv_path = "organizations_percentages_dataset_final.csv"
df = pd.read_csv(csv_path)

# needed to ignore Organization Name column
feature_cols = [c for c in df.columns if c.startswith("chart_family.") or c.startswith("data_context.") or c.startswith("visual_embellishments.") or c.startswith("structural_features.")]

# holding our features
X = df[feature_cols].copy()

# holding the responding organization names 
org_col = "Organization Name"
org_names = df[org_col].copy()

# making feature more readable 
pretty_feature_names = []
for c in feature_cols:
    new_c = c
    new_c = new_c.replace("chart_family.", "CF: ")
    new_c = new_c.replace("data_context.", "DC: ")
    new_c = new_c.replace("structural_features.", "SF: ")
    new_c = new_c.replace("visual_embellishments.", "VE: ")
    new_c = new_c.replace("_", " ")
    pretty_feature_names.append(new_c)

X.columns = pretty_feature_names

# ====== STANDARDIZE FEATURES

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, index=org_names, columns=X.columns)

# ======= Hierarchical clustering (Ward)

row_linkage = linkage(X_scaled_df.values, method="ward")
n_clusters = 5
cluster_labels = fcluster(row_linkage, t=n_clusters, criterion="maxclust")

cluster_df = pd.DataFrame({
    "Organization Name": org_names,
    "Cluster": cluster_labels
}).sort_values(["Cluster", "Organization Name"])

# output the cluster memberships to the terminal
print("\nCluster memberships:\n")
for clust in sorted(cluster_df["Cluster"].unique()):
    members = cluster_df.loc[cluster_df["Cluster"] == clust, "Organization Name"].tolist()
    print(f"Cluster {clust}:")
    for m in members:
        print(f"  - {m}")
    print()

# ========= Clustered heatmap 

# --- designing cluster palette
cluster_palette = {
    1: "#4E79A7",
    2: "#E15759",
    3: "#59A14F",
    4: "#B07AA1",
    5: "#F28E2B",
    6: "#76B7B2"
}
row_colors = pd.Series(cluster_labels, index=org_names).map(cluster_palette)

# --- creating heatmap

sns.set_theme(style="white", font_scale=0.9)

g = sns.clustermap(
    X_scaled_df,
    row_linkage=row_linkage,
    col_cluster=False,
    row_colors=row_colors,
    cmap="vlag",
    center=0,
    linewidths=0.4,
    linecolor="#D9D9D9",
    figsize=(18, 12),
    xticklabels=True,
    yticklabels=True,
    cbar_kws={"label": "Standardized Feature Value (z-score)"}
)

# ---- fixing legend or scale
g.cax.remove()

cbar_ax = g.fig.add_axes([0.92, 0.8, 0.02, 0.20])  
norm = plt.Normalize(vmin=X_scaled_df.values.min(), vmax=X_scaled_df.values.max())
sm = plt.cm.ScalarMappable(cmap="vlag", norm=norm)
sm.set_array([])

cbar = g.fig.colorbar(sm, cax=cbar_ax)
cbar.set_label("z-Score", rotation=270, labelpad=15)

# ---- basic visualization attributes: title, labels, etc.
g.ax_heatmap.set_title(
    "Hierarchical Clustering of Organizations by Visualization Repertoire",
    pad=20,
    fontsize=14,
    fontweight="bold"
)

g.ax_heatmap.set_xlabel("Visualization Features", fontsize=11)
g.ax_heatmap.set_ylabel("Organizations", fontsize=11)

plt.setp(g.ax_heatmap.get_xticklabels(), rotation=60, ha="right", rotation_mode="anchor")
plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)

# saving figure
g.savefig("organization_clustered_heatmap_corner_cbar.png", dpi=300, bbox_inches="tight")

# ======= PCA projection as a simple 2D cluster 

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled_df.values)

plot_df = pd.DataFrame({
    "Organization Name": org_names,
    "PC1": X_pca[:, 0],
    "PC2": X_pca[:, 1],
    "Cluster": cluster_labels
})

# --- creating scatterplot

plt.figure(figsize=(11, 8))
ax = sns.scatterplot(
    data=plot_df,
    x="PC1",
    y="PC2",
    hue="Cluster",
    palette=cluster_palette,
    s=120,
    edgecolor="white",
    linewidth=0.8
)

for _, row in plot_df.iterrows():
    ax.text(
        row["PC1"] + 0.03,
        row["PC2"] + 0.03,
        row["Organization Name"],
        fontsize=8
    )

# ---- basic visualization attributes: title, labels, etc.

ax.set_title(
    "PCA Projection of Organizational Visualization Repertoires",
    fontsize=14,
    fontweight="bold"
)
ax.set_xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% var.)")
ax.set_ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% var.)")
ax.legend(title="Cluster", frameon=False)

# saving figure
sns.despine()
plt.tight_layout()
plt.savefig("organization_cluster_pca.png", dpi=300, bbox_inches="tight")


# ====== saving cluster assignments

cluster_df.to_csv("organization_cluster_assignments.csv", index=False)
