# Complete Codebook - All Labels in our Dataset 

## File Information and Metadata 
- Organization Name
  - Description: Full organization name used in our study.
  - Type: Text
- Organization Acronym 
  - Description: Our self-assigned acronym from the organization name.
  - Type: Text
- Organization Type
  - Description: Organization classification: National Agency, Nonprofit, or International Agency
  - Type: Text
- Directory Index Page URL
  - Description: The search directory index page that the web scraper was on prior to opening the linked web page (if applicable) where the visualization was found.
  - Type: URL
- Directory Keyword 
  - Description: The keyword used in the search directory to find this visualization.
  - Type: Text
- Directory Link URL 
  - Description: The linked web page off of the search directory index page that the visualization was scraped from or found.
  - Type: URL
- Date Scraped
  - Description: Date the web scraper collected the visualization. 
  - Type: Date
- Last Modified
  - Description: Last-Modified field in the HTTP Response (if applicable) from the linked web page.
  - Type: Date, Null (Denoted as Not Found in csv)
- Webpage Title 
  - Description: Title tag in the HTML content from linked web page (if applicable) that the visualization was found. 
  - Type: Text, Null (Blank in csv)
Webpage Author
  - Description: Author tag in the HTML content from linked web page (if applicable) that the visualization was found. 
  - Type: Text, Null (Denoted as Blank or Not Found in csv)
- Webpage Description
  - Description: Description tag in the HTML content from linked web page (if applicable) that the visualization was found. 
  - Type: Text, Null (Denoted as Blank or Not Found in csv)
- Image URL
  - Description: The exact URL that stored the visualization on the organizations website. 
  - Type: URL
- Visualization Name 
  - Description: The filename of the scraped visualization.
  - Type: Filename (Filename assignment is described at the bottom of this section)
- Visualization Text
  - Description: The text grabed from the Pytesseract, which is a Python wrapper for Google's Tesseract OCR Engine.
  - Type: Text

Note: File naming convention is as follows: organization_acronym-url_id-health-image_scraped_number. organization_acronym is the self-assigned acyonym from researchers. url_id is the primarykey we used when web scraping. health is the simply field of the organizations; all files include the word health. Image scraped number is the count of how many images were scraped associated with the url id, at the time this image was scraped.
    
## Chart Family and Data Context
- cf.chart_type_primary 
  - Description: Assigns the primary chart family of the described options, e.g., line chart, bar chart, area chart, etc. 
  - Type: Text
- cf.chart_type_secondary
  - Description: Assigns the secondary chart family (if applicable). 
  - Type: Text
- dc.data_context_primary (MH: Add number of options, examples)
  - Description: Assigns the primary data context of the described options, e.g., temporal_trend, hierarchical, categorical_comparison, etc. 
  - Type: Text
- dc.data_context_secondary
  - Description: Assigns the secondary data context.  
  - Type: Text


## Structural Features 
- sf.multi_panel
  - Description: Evaluates if the visualization containes multiple panels. 
  - Type: Boolean
- sf.axes_labeled
  - Description: Evaluates if the visualization has labeled axes.
  - Type: Boolean
- sf.missing_data_present 
  - Description: Evaluates if the visualization has denoted missing data. 
  - Type: Boolean
- sf.has_direct_labels
  - Description: Evaluates if the visualization has direct labels. 
  - Type: Boolean
- sf.has_legend
  - Description: Evaluates if the visualization has a legend.
  - Type: Boolean
- sf.has_grid_lines
  - Description: Evalautes if the visualization has grid lines.
  - Type: Boolean
- sf.has_title
  - Description: Evalautes if the visualization has title.
  - Type: Boolean
- sf.has_y_axis
  - Description: Evaluates if the visualization has a y axis.
  - Type: Boolean
- sf.has_x_axis
  - Description: Evaluates if the visualization has a x axis.
  - Type: Boolean
  
## Visual Embellishments 
- ve.iconography_present 
  - Description: Evaluates if iconography was present in the visualization.
  - Type: Boolean
- ve.photograph_present
  - Description: Evaluates if a photograph was present in the visualization.
  - Type: Boolean
- ve.medical_imaging_present
  - Description: Evaluates if a medical imaging was present in the visualization.
  - Type: Boolean
- ve.datapoints_shapes_lines
  - Description: Evaluates if the data points were unique shapes or have different marked lines.
- ve.has_text_annotations
  - Description: Evaluates if the visualization has text annotations. 
  - Type: Boolean

## Color & Text Density 
- color.color_values
  - Description: The assigned HEX codes for the colors observed by GPT.
  - Type: List
- color.color_blind_risky
  - Descroption: Determined to have a risky pair of colors under normal or CVD conditions such as protanomaly, deuteranomaly, and tritanomaly.
  - Type: Boolean
- color.grayscale
  - Description: Determined to only have grayscale colors in the image, e.g., white, gray, and black.
  - Type: Boolean
- color.number_of_colors
  - Description: Count of colors with a threshold of saturation and hue in the visualization. For instance, we don't include white, gray, and black colors in the count.
  - Type: Number
- color.hsv_names
  - Description: List of our assigned HSV names.
  - Type: List
- td.text_density 
  - Description: Text density level of the visualization.
  - Type: Text (Low, Middle, High)
