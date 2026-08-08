# Charting Public Health 

## Introduction
### High-Level 
This GitHub repo is the associated visualization dataset, figures, and important code for the IEEE VIS 2026 Submission "Charting Public Health: A Taxonomic Study of Visualization Practices in the Public Health Field." The following information describes the content you'll find in each directory or file. The ReadMe ends by describing the packages used (and those that need to be installed) to run the scripts included in our repo. (Note: will add the formal citation soon!) 

### Abstract
Public health organizations regularly produce and publish data visualizations to raise awareness of critical issues, influence decision-making processes, and promote overall well-being. However, the design practices shaping these visualizations in real-world settings remain largely unexamined, limiting the research community's ability to evaluate their effectiveness, accessibility, and alignment with communication goals. To address this gap, we construct and analyze a large-scale corpus of over 4,000 real-world data visualizations drawn from more than two dozen websites associated with U.S. and international public health organizations. We evaluate salient design characteristics like chart type, visualization accessibility, use of embellishments like iconography, and design flaws. This work contributes to understanding real-world decisions in designing data visualizations and supports public health officials in improving data visualization-related communications. 

## Repo Structure
- **Dataset:** The directory includes the complete dataset (either in CSV or JSON format) consisting of each visualization file's information and metadata, chart family, data context, structural features, visual embellishments, color, and text density. 

- **Measurements:** Python scripts that show our computation of Text Density, Color Accessibility Risk, and HSV Color Assignments (consisting of the derived variables: palette size, if the visualization is grayscale, HSV color names assignment). 

- **Paper Charts:** Image files (PNG or PDF) of the charts in the paper: design profiles, a global view of design practices, and evaluating risky pairs in color accessibility measurement. 

- **PCA Work:** Python scripts used to evaluate Visualization Design Profiles: Statistical, Institutional, Narrative, Scientific, and Outlier.  Within the PCA Work, we used a dataset that described each organization's visualization corpus by evaluating the percentage of a particular label (e.g., has text annotation or is a bar chart) within that corpus. In our PCA scripts, we standardized all label measurements within that dataset. Note: figures produced in those scripts were for internal analytical use only—they're not featured in the paper.

- **Visualizations:** Image files of the 4,171 visualizations within our final corpus. Note: 114 image files were removed due to potential copyright. More information can be found in the Disclaimer below. 

- **Codebook.md:** A complete codebook of all the tags featured in the dataset. 

- **Prompts.md:** Markdown file that lists all prompts used for GPT tagging. Note: some tags are excluded from the visualization dataset because they were outside our main investigations, redundant, or exhibit inconsistent behavior.

- **archived_urls.csv:** 
  Generated archived webpages related to our visualization corpus with the Internet Archive, Save Page Now API. 

## Technical Items 
### Prerequisites & Needed Materials
We use the following Python packages in the code files included in this repository. 

**Standard Libraries**
- OS
- pathlib
- numpy
- re
- itertools
- colorsys

**Third-Party Libraries**
- Pillow - Python Imaging Library (PIL)
- pandas
- colorspacious
- scikit-image
- matplotlib
- seaborn
- scikit-learn
- scipy

## Disclaimer 
**Statement:** Visualizations collected from 26 public health organizations, the majority of which are U.S. government agencies whose visualizations are in the public domain. Data collection was limited to publicly available web pages. We have released the complete set of public-domain visualizations, along with the derived annotations, metadata, codebook, and analysis scripts, creating a resource for future research. Visualizations from nonprofit and international organizations cannot be redistributed because they may remain the intellectual property of their respective organizations; for these cases, we provide annotations and metadata to facilitate retrieval from the original sources where permitted. Researchers using the corpus for downstream applications, including computational model development, should ensure that their use complies with applicable copyright, licensing, and website terms.

**Consideration:** We have removed a total of 114 visualizations from the Visualizations because they're distributed from nonprofit and international organizations. Dataset files still have the metadata and features associated with these images to facilitate retrieval as described previously. 
