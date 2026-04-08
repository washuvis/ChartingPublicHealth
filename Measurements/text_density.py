import os
import pandas as pd 
from pathlib import Path
from PIL import Image
import numpy as np
import re

# method used to find our low, middle, and high text density distinctions. 
def text_levels(): 

    # reading in labels 
    visualizations = pd.read_csv("./Dataset/visualizations_labels.csv")

    # list to hold each visualization's computed text density
    edited_all_vis_text = []

    # iterate through each visualization 
    for index, row in visualizations.iterrows():

        # grabbing vis text
        vis_text = row["Visualization Text"]
        vis_name = row["Visualization Name"]

        # cleaning the text -- removing newlines and keeping only alphabetical characters. 
        vis_text = vis_text.strip().replace("\n", "")
        edited_vis_text = re.sub(r'[^a-zA-Z]', '', vis_text)

        # computing the number of characters in the edited text
        edited_vis_character_count = len(edited_vis_text)

        try:
            file_path = os.path.join("Visualizations", vis_name)

            # computing image size and calculating text_density
            with Image.open(file_path) as img:
                width, height = img.size

                area = width * height 

                # text density is equal to the number of characters divided image area 
                text_density = edited_vis_character_count / area 

                # append to the list
                edited_all_vis_text.append(text_density)

        except Exception as e:
                print(f"An error occurred with {vis_name}: {e}")
        

    # computing the IQR range of the text density of visualizations in the collection
    print("------ TEXT DENSITY PERCENTILES --------")
    edited_quartiles = np.quantile(edited_all_vis_text, [0.25, 0.5, 0.75])
    edited_Q1 = edited_quartiles[0]
    edited_Q2 = edited_quartiles[1]
    edited_Q3 = edited_quartiles[2]

    print(f"Q1 (25th percentile): {edited_Q1}")
    print(f"Q2 (Median, 50th percentile): {edited_Q2}")
    print(f"Q3 (75th percentile): {edited_Q3}")

    return edited_quartiles


text_levels()