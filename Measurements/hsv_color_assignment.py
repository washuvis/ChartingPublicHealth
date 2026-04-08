import pandas as pd 
import numpy as np
import colorsys 
from pathlib import Path

# dictionary that holds our decided colors and their hue ranges in this study. 
COLOR_RULES = {
    "pink": {
        "hue": [(0, 20), (340, 360)],
        "v_min": 0.75
    },
    "brown": {
        "hue": [(15, 45)],
        "v_max": 0.6
    },
    "red": {
        "hue": [(0, 15), (345, 360)]
    },
    "orange": {
        "hue": [(15, 45)]
    },
    "yellow": {
        "hue": [(45, 65)]
    },
    "green": {
        "hue": [(65, 150)]
    },
    "teal": {
        "hue": [(150, 190)]
    },
    "blue": {
        "hue": [(190, 230)]
    },
    "indigo": {
        "hue": [(230, 255)]
    },
    "purple": {
        "hue": [(255, 345)]
    }
}

# a list that determines order of the colors in each iteration 
COLOR_ORDER = [
    "pink",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "teal",
    "blue",
    "indigo",
    "purple"
]

# checking if the hue is in range 
def in_hue_ranges(h, ranges):
    return any(low <= h < high for (low, high) in ranges)
    
# assigining name of each color with saturation above s > 0.15, determing if the visualization is grayscale only (s < 0.15,
# and counting all colors NOT apart of grayscake.

# classify colors hsv produces three variables: color names, color count, and grayscale. 
# 1) assigns names, e.g., pink, orange, or teal, from the converted hsv values from the tagged colors from GPT
# 2) counts the number of colors in the tagged colors or palette size. all counted colors are NOT gray, white, or black or saturation is above 0.15. 
# 3) marks true or false with grayscale. if true, then there's no color beside gray, white, or black in the visualization.
def classify_colors_hsv(vis_colors):

    # creating variables to store information
    results = []                # name of the colors
    color_count = 0             # number of colors (excluding gray, white, and black)
    color_identified = False    # remarks if a color with a saturation above 0.15 was observed, e.g., pink, teal, and purple.
    grayscale_vis = False       # holds the classification if the visualization is grayscale


    # converting encoding of string to list 
    vis_colors = vis_colors.replace("[", "").replace("]", "").replace('"', "")
    vis_colors_list = vis_colors.split(',')
    vis_colors_list = [color.strip() for color in vis_colors_list]

    # iterate thru every code in the list
    for hex_color in vis_colors_list:

        # converting hex to rgb
        hex_color = hex_color.lstrip('#')
        r,g,b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        # converting rgb to hsv
        r_n, g_n, b_n = r/255, g/255, b/255 # Normalize to [0,1] for colorsys
        h, s, v = colorsys.rgb_to_hsv(r_n, g_n, b_n)
        h = h * 360  # convert to degrees

        # holds the color that is closest to the parameters of the hsv value
        closest_name = None
        
        # handles low saturation: gray, white, and black
        if s < 0.15:
            if v > 0.85:
                closest_name = "white"
            elif v < 0.2:
                closest_name = "black"
            else:
                closest_name = "gray"


        # rule-based classification for assigning specified hues in COLOR_RULES and the hsv is above or eqaul to 0.15 in saturation
        else: 
            # a color with saturation above 0.15 has been observed
            color_identified = True 

            # counting the number of colors the visualizations has (outside of white, black, and gray)
            color_count = color_count + 1 

            # iterate thru colors described in our hsv classifications
            for color in COLOR_ORDER:

                rules =  COLOR_RULES[color]

                if not in_hue_ranges(h, rules["hue"]):
                    continue
                
                # check optional constraints: v_min, v_max, and s_man
                if "v_min" in rules and v < rules["v_min"]:
                    continue
                if "v_max" in rules and v > rules["v_max"]:
                    continue
                if "s_min" in rules and s < rules["s_min"]:
                    continue
                
                # if reaching this code of line, means the current hsv color falls in hue_ranges and/or corresponds with optional constraints
                closest_name = color
                break

            
        results.append(closest_name)
    
    # if color_identified is false, then the visualization is grayscale. no color was observed with a greater saturation thann 0.15.
    if color_identified == False: 
        results = []
        grayscale_vis = True


    # results is the hsv color names, grayscale_vis is the boolean variable if it's grayscale, 
    # and color_count is the number of colors or palette size (with a specified hue in COLOR_RULES and with a saturation above 0.15)
    return results, grayscale_vis, color_count

# picking a random visualization from our dataset and returning three variables: hsv color names, grayscale boolean variable, and palette size (or number of colors). 
# this is just an example, one can easily infer how we made this step iterative and assigned them to all visualizations. 
def example_run():
    # read in our dataset
    script_dir = Path(__file__).parent
    file_path = script_dir.parent / "Dataset" / "visualizations_labels.csv"
    visualizations_labels = pd.read_csv(file_path)

    # grab a random visualization's index 
    random_index = visualizations_labels.sample(n=1).index[0]
    vis_name = visualizations_labels.at[random_index, 'Visualization Name']

    # grab important information and place them as arguments to classify_colors_hsv
    hex_colors = visualizations_labels.at[random_index, 'color.color_values']
    hsv_names, grayscale, palette_size = classify_colors_hsv(hex_colors) 

    print(f"----- {vis_name} -----")
    print(f"HSV ASSIGNMENTS: {hsv_names}")
    print(f"Is the visualization grayscale? : {grayscale}")
    print(f"What is the palette size of the visualization? (excluding grayscale associated colors): {palette_size}")

example_run()
