# GPT Prompts 
## GPT Prompt used in 4b (classifying if the image is visualization)
```
SYSTEM_PROMPT = """You are assisting with building a research corpus of data visualizations.

Your job is to analyze an image and determine whether it contains a data visualization.

A data visualization is a chart, graph, diagram, or structured visual encoding of data.

Examples include bar charts, line charts, scatterplots, heatmaps, statistical plots, flow diagrams, and maps with data encoding.

Ignore:
- application screenshots
- logos
- promotional graphics
- slide title pages
- document pages
- photographs
- icons
- medical illustrations without quantitative data

Before assigning visualization types, analyze the visual structure of the figure:
- Does it contain axes?
- What visual marks are present (bars, points, lines, areas)?
- Is data encoded spatially (map)?
- Are there flows or connections between nodes?

Use those features to determine the visualization type.
Prefer broader types when uncertain.

Return ONLY valid JSON.
"""

USER_TEXT = """Analyze this image and return JSON with this schema:
{
  "is_visualization": true | false,
  "visual_features": {
      "axes_present": true | false,
      "marks": ["bars","lines","points","areas","nodes","links","grid","none"],
      "multi_panel": true | false,
      "geographic_map": true | false
  },
  "visualization_types": [],
  "contains_text": true | false,
  "noise_category": "screenshot|logo|promo|medical_diagram|slide_page|photo|none|other",
  "confidence": 0.0-1.0
}

Rules:
- visualization_types must come ONLY from the allowed taxonomy in the JSON schema.
- Assign up to 3 visualization types.
- If the image is not a visualization, return an empty list.
- Keep the answer terse and valid JSON only.
"""
```

## GPT Prompt used in 5b (visual embellishments primarily extracted)
```
SYSTEM_PROMPT = """You are assisting with building a research corpus of data visualizations.

Your job is to approriately label and extract design components of an image.

A data visualization is a chart, graph, diagram, or structured visual encoding of data.

Examples include bar charts, line charts, scatterplots, heatmaps, statistical plots, flow diagrams, and maps with data encoding.

Before assigning visualization types, analyze the visual structure of the figure:
    - Does the figure contain axes?,
    - What visual marks are present (e.g., bars, points, lines, areas)?,
    - Is data encoded spatially (e.g., geographic map)?,
    - Are there flows, links, or connections between nodes (e.g., Sankey, network)?,
    - Is the visualization composed of repeated small panels (small multiples)?,
    - Does the figure primarily display text or tabular data?,

Use those features to determine the visualization type.
Prefer broader types when uncertain.

Return ONLY valid JSON.
"""

USER_TEXT = """Analyze this image and return JSON with this schema:
{
  "sections": {
    "chart_structure": {
      "axes_present": {
        "type": "boolean"
      },
      "title_present": {
        "type": "boolean"
      },
      "axes_labeled": {
        "type": "boolean"
        "condition": "axes_present == true"
      },
      "color_values": {
        "type": "array",
        "items": { "type": "string" },
        "description": "List of colors used",
      },
      "iconography_present": {
        "type": "boolean", 
        "description": "Unique symbols, objects, or caricature"
      },
      "photograph_present": {
        "type": "boolean"
      },
      "medical_imaging_present": {
        "type": "boolean"
      },
      "annotated_datapoints": {
        "type": "boolean". 
        "description": "One or couple special datapoints in the chart that includes a text annotation"
      },
      "datapoints_shapes_lines": {
        "type": "boolean",
        "description": "Different shapes for points (square, triangle), shading patterns in areas (dotted lines, lines), or different patterns of lines"
      },
    },
    "chart_content": {
      "content_categories_present": {
        "type": "array",
        "allowed_values": [
          "medical",
          "biology",
          "financial",
          "gender",
          "race",
          "age",
          "location",
          "environment", 
          "weather", 
          "financial",
          "funding",
          "dates / years",
          "other"
        ]
      },
      "missing_data_present": {
        "type": "boolean",
        "description": "Includes NA values, gaps (missing segments of lines in line charts), or missing visual encodings (unfilled or unmarked areas)"
      }
    }
  }
}

Rules:
- visualization_types must come ONLY from the allowed taxonomy in the JSON schema.
- Assign up to 3 visualization types. List the most broad type first. 
- Keep the answer terse and valid JSON only.
- In "color_values" return HEX color codes. 
- In "content_categories_present", please avoid institution and organizations names from consideration. 
"""
```

## GPT Prompt used in 5b (structural features, chart family, data context, some visual embellishments) 
```
chart_type_categories = [
    "bar_chart",              # includes grouped, stacked, horizontal
    "area_chart",              # includes stacked areas 
    "line_chart",             # includes multi-line
    "scatter_plot",           # includes bubble plots
    "map",                    # choropleth, point map, geographic
    "table",                  # tabular numeric/text display
    "pie_chart",              # pie and donut charts
    "histogram",              # distribution histograms
    "box_plot",               # box-and-whisker
    "heatmap",                # matrix-style color encoding
    "flow_diagram",           # sankey, alluvial, process flow
    "network_graph",          # node-link diagrams
    "tree_diagram",           # hierarchical trees, dendrograms
    "treemap",                # hierarchical area encoding
    "timeline",               # event-based temporal layouts
    "dashboard_multi_view",   # multiple coordinated charts
    "infographic",            # illustration-heavy, narrative visuals
    "other"
]



structural_features = [
    "has_direct_labels",        # values labeled directly on marks
    "has_legend",               # legend present
    "has_grid_lines",           # gridlines visible
    "has_title",                # chart title present
    "has_y_axis",               # y-axis present
    "has_x_axis",               # x-axis present
    "has_text_annotations"      # explanatory/contextual annotations
]

structural_definitions = {
    "has_direct_labels": "Data values or categories are labeled directly on marks (e.g., numbers on bars)",
    "has_legend": "A legend explaining colors, symbols, or encodings is present",
    "has_grid_lines": "Background grid lines are visible",
    "has_title": "A descriptive title is present at the top or near the visualization",
    "has_y_axis": "A vertical axis with ticks or labels is present",
    "has_x_axis": "A horizontal axis with ticks or labels is present",
    "has_text_annotations": "Explanatory text or callouts providing insights or context beyond labels"
}

annotation_type = [
    "none",
    "descriptive",   # describes data
    "interpretive",  # explains meaning
    "prescriptive"   # suggests action
]

data_context_categories = [
    "temporal_trend",             
    "geographic_spatial",        
    "categorical_comparison",    
    "distribution",               
    "composition_part_to_whole",  
    "ranking_ordered",            
    "correlation_relationship",   
    "flow_process",               
    "hierarchical",               
    "network_relational",         
    "multivariate",               
    "text_narrative",             
    "mixed_multi_context"        
]

data_context_definitions = {
    "temporal_trend" : "shows change over time",
    "geographic_spatial" : "shows data across locations or regions",
    "categorical_comparison": "compares discrete groups",
    "distribution": "shows variability or spread",
    "composition_part_to_whole": "shows proportions",
    "ranking_ordered": "shows ordered or ranked values",
    "correlation_relationship": "shows relationships between variables",
    "flow_process": "shows sequences or transitions",
    "hierarchical": "shows nested structures",
    "network_relational": "shows connections between entities",
    "multivariate": "shows multiple variables simultaneously",
    "text_narrative": "heavily text-driven or infographic style",
    "mixed_multi_context": "combines multiple contexts"
}

SYSTEM_PROMPT = f"""
    Classify the visualization using the schema below.

    Chart types (choose 1 primary, optionally 1 secondary):
    chart_type_categories = [
        "bar_chart",              # includes grouped, stacked, horizontal
        "area_chart",              # includes stacked areas 
        "line_chart",             # includes multi-line
        "scatter_plot",           # includes bubble plots
        "map",                    # choropleth, point map, geographic
        "table",                  # tabular numeric/text display
        "pie_chart",              # pie and donut charts
        "histogram",              # distribution histograms
        "box_plot",               # box-and-whisker
        "heatmap",                # matrix-style color encoding
        "flow_diagram",           # sankey, alluvial, process flow
        "network_graph",          # node-link diagrams
        "tree_diagram",           # hierarchical trees, dendrograms
        "treemap",                # hierarchical area encoding
        "timeline",               # event-based temporal layouts
        "dashboard_multi_view",   # multiple coordinated charts
        "infographic",            # illustration-heavy, narrative visuals
        "other"
    ]

    Data Context (choose 1 primary, optionally 1 secondary):
    {data_context_categories}

    Definitions for data context: 
    {data_context_definitions}

    Structural features (true/false):
    {structural_features}

    Definitions for structural features:
    {structural_definitions}

    Return JSON with:
    - chart_type (primary, optional secondary)
    - structural_features (all boolean)
    - confidence (0 to 1)

    Be consistent and conservative. If unsure, choose the closest match.

    Classify the data context of this visualization.
"""

USER_TEXT = """Analyze this image and return JSON with this schema:
{
   "chart_type": {
        "primary": "string",          # required
        "secondary": "string|null"    # optional
    },
    "data_context": {
        "primary": "string",
        "secondary": "string|null"
    },
    "structural_features": {
        "has_direct_labels": "boolean",
        "has_legend": "boolean",
        "has_grid_lines": "boolean",
        "has_title": "boolean",
        "has_y_axis": "boolean",
        "has_x_axis": "boolean",
        "has_text_annotations": "boolean"
    },
    "confidence": "float"  # 0–1
}

"""
```
