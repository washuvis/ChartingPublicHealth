# Charting-Public-Health 
Welcome! 
This GitHub repo is the associated visualization dataset, figures, and important code to IEEE VIS 2026 Submission "Charting Public Health: A Taxonomic Study of Visualization Practices in the Public Health Field."

## Dataset
Directory includes the complete dataset (either in CSV or JSON format) consisting of each visualization file information and metadata, chart family, data context, structural features, visual embellishments, color, and text density. 

## Measurements 
Python scripts that show our computation of Text Density, Color Accessibility Risk, and HSV Color Assignments (consisting of the derived variables: palette size, if the visualization is grayscale, HSV color names assignment). 

## PCA Work 
Python scripts used to evaluate Visualization Design Profiles: Statistical, Institutional, Narrative, Scientific, and Outlier. 

## Visualizations 
All image files of the 4,285 visualizations within our final corpus. 

## Codebook.md 
A complete codebook of all the tags featured in the dataset. 

## Prompts.md 
Markdown file that lists all prompts used for GPT tagging. Note, some tags are excluded from the visualization dataset due to being outside of our main investigations, redundant, and inconsistent behavior.  

## Packages
We use the following Python packages in the code files included in this repository. 

### Standard Libraries
- OS
- pathlib
- numpy
- re
- itertools

### Third-Party Libraries
- Pillow - Python Imaging Library (PIL)
- pandas
- colorsys
- colorspacious
- scikit-image
