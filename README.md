# COMP4037-diet-visualization
Interactive Dash App comparing environmental impacts of diet types (COMP4037)
The dashboard visualizes the environmental impacts of different dietary groups using a Parallel Coordinates Plot, allowing for multivariate comparison across 8 key environmental indicators.
Features

- Interactive filters for sex and age group
- Multivariate comparison across 8 environmental variables:
  - Greenhouse Gas Emissions
  - Land Use
  - Water Scarcity
  - Eutrophication Potential
  - CH₄ Emissions
  - N₂O Emissions
  - Biodiversity Impact
  - Agricultural Water Use
- Color-coded diet group representation
- Hover details for subgroup analysis
- Built using Dash,Plotly, and Pandas

Files Included
interactive_diet_visualizer_corrected_FINAL.py Main Dash application script                      
normalized_diet_data.csv                Preprocessed dataset using Min-Max normalization 

Dataset Conversion (Normalization)

The original dataset was transformed by:
- Grouping by diet_group
- Selecting key environmental metrics
- Applying **Min-Max scaling** to bring all values to a 0–1 range

 How to Run the App

### 1. Install dependencies
```bash
pip install dash plotly pandas
Run python interactive_diet_visualizer_corrected_FINAL.py
Visit http://127.0.0.1:8050 in your browser.


