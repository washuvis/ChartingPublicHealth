# Charting-Public-Health 
Welcome! 
This GitHub repo is the associated visualization dataset, figures, and important code to IEEE VIS 2026 Submission "Charting Public Health: A Taxonomic Study of Visualization Practices in the Public Health Field." The following information describes the content you'll find in each directory or file. The ReadMe ends describing the packages used (and needed to be installed) to run the scripts included in our repo.

## Dataset
Directory includes the complete dataset (either in CSV or JSON format) consisting of each visualization file information and metadata, chart family, data context, structural features, visual embellishments, color, and text density. 

## Measurements 
Python scripts that show our computation of Text Density, Color Accessibility Risk, and HSV Color Assignments (consisting of the derived variables: palette size, if the visualization is grayscale, HSV color names assignment). 

## Paper Charts
Image files (PNG or PDF) of our interesting charts in the paper: desgin profiles, global view of design practices, and evaluating risky pairs in color accessibility measurement. 

## PCA Work 
Python scripts used to evaluate Visualization Design Profiles: Statistical, Institutional, Narrative, Scientific, and Outlier.  Within the PCA Work, we used a dataset that described each organization's visualization corpus by evaluating the percentage of a particular label, e.g., has text annotation or is bar chart, within that corpus. In our PCA scripts, we standarized all labels measurements within that dataset. Note, figures produced in those scripts were for internal analytical use only -- they're not featured in the paper.

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
- colorsys

### Third-Party Libraries
- Pillow - Python Imaging Library (PIL)
- pandas
- colorspacious
- scikit-image
- matplotlib
- seaborn
- scikit-learn
- scipy

