import pandas as pd 
import numpy as np
from pathlib import Path
from itertools import combinations
from colorspacious import cspace_convert
from skimage.color import rgb2lab, deltaE_ciede2000

# ---- simulate color vision deficiency. deficiencies we consider are protanomaly, deuteranomaly, or tritanomaly.
def simulate_cvd(rgb_colors: np.ndarray, deficiency: str, severity: int = 100) -> np.ndarray:
    spec = {
        "name": "sRGB1+CVD",
        "cvd_type": deficiency,
        "severity": severity
    }
    simulated = cspace_convert(rgb_colors, spec, "sRGB1")
    return np.clip(simulated, 0, 1)


# ---- computes pairwise perceptual distances with CIEDE2000
def lab_distances(rgb_colors: np.ndarray) -> dict:

    lab = rgb2lab(rgb_colors[np.newaxis, :, :])[0]

    dists = {}
    for i, j in combinations(range(len(lab)), 2):
        d = deltaE_ciede2000(
            lab[i][np.newaxis, :],
            lab[j][np.newaxis, :]
        )[0]
        dists[(i, j)] = float(d)

    return dists

# ---- evaluates if the hex codes tagged in the visualization contain any risky pairs. 
def evaluate_palette(hex_codes, threshold=5):
    
    # -- converting hex to rgb
    rgb_list = []

    for hex_color in hex_codes: 
        hex_color = hex_color.strip().lstrip("#")
        rgb_color = np.array([
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16)
        ]) / 255.0
        rgb_list.append(rgb_color)

    rgb = np.array(rgb_list)

    # -- simulating and storing normal and CVD conditions. CVD conditions are with a severity of 100. 
    conditions = {
        "normal": rgb,
        "protanomaly": simulate_cvd(rgb, "protanomaly", severity=100),
        "deuteranomaly": simulate_cvd(rgb, "deuteranomaly", severity=100),
        "tritanomaly": simulate_cvd(rgb, "tritanomaly", severity=100),
    }

    # -- finding any risky pairs
    results = {}

    # iterate thru rgb colors under the specified conditions 
    for condition, sim_rgb in conditions.items():

        # compute distance between pairs
        pair_dists = lab_distances(sim_rgb)

        # finding the risky pair
        risky_pairs = [
            {
                "pair": (hex_codes[i], hex_codes[j]),
                "distance": round(dist, 2)
            }
            for (i, j), dist in pair_dists.items()
            if dist < threshold
        ]

        # storing the risky pair in our results 
        results[condition] = {
            "min_distance": round(min(pair_dists.values()), 2),
            "risky_pairs": sorted(risky_pairs, key=lambda x: x["distance"])
        }

    return results

# --- evaluates if any of the hex codes in a filename contains a risky pair. if so, then return true. if not, return false. 
def color_blind_accessibility(filename, colors): 

    # setting up variables 
    vis_name = filename
    vis_colors = colors
    color_accessibility_risky = False
    
    # converting encoding of string to list 
    vis_colors = vis_colors.replace("[", "").replace("]", "").replace('"', "")
    vis_colors_list = vis_colors.split(',')
    vis_colors_list = [color.strip() for color in vis_colors_list]

    # if there is only one color in the list, then skip. cannot compare pairs, then. 
    # note: there's only 13 visualizations that only have one hex color assigned. 
    if len(vis_colors_list) == 1:
        return color_accessibility_risky

    # get the results from evaluate_palette 
    results = evaluate_palette(vis_colors_list, threshold=5)

    # iterate thru the results and see if there exists a risky pair 
    # if so, then update the boolean variable as true and break. 
    for condition, info in results.items():
        if info["risky_pairs"]:
            color_accessibility_risky = True
            break
    
    return color_accessibility_risky

# picking a random visualization from our dataset and assigning if it's risky or not in terms of color accessibility. 
# this is just an example, one can easily infer how we made this step iterative and assigned them to all visualizations. 
def example_run():
    # read in our dataset
    script_dir = Path(__file__).parent
    file_path = script_dir.parent / "Dataset" / "visualizations_labels.csv"
    visualizations_labels = pd.read_csv(file_path)

    # grab a random visualization's index 
    random_index = visualizations_labels.sample(n=1).index[0]

    # grab important information and place them as arguments to color_blind_accessibility
    vis_name = visualizations_labels.at[random_index, 'Visualization Name']
    hex_colors = visualizations_labels.at[random_index, 'color.color_values']
    risky = color_blind_accessibility(vis_name, hex_colors) 

    # reporting decision 
    if risky == True: 
        print("RISKY PAIR FOUND")
        print(f"{vis_name} : contains at least one risky pair of colors.")
    else: 
        print("RISKY PAIR WAS NOT FOUND")
        print(f"{vis_name} : DOES NOT contain a single risky pair of colors.")

example_run()

