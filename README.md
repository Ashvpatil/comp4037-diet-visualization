COMP4037-diet-visualization
Interactive Dash App showing the comparison of environmental impacts of different diet types (COMP4037)

The dashboard visualizes the environmental impacts of each dietary group using Parallel Coordinates Plot which provides a multivariate comparison of 8 key indicators of the environment.

Features:-
- Interactive filters for **sex** and **age group**
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
- Built using **Dash**, **Plotly**, and **Pandas**

Files Included:-
- interactivedietvisualizercorrectedFINAL.py Main application script of Dash.
- normalizeddietdata.csv Preprocessed dataset created through Min-Max normalization.

Dataset conversion (normalization)
Accomplished through:
- Grouping by diet_group
- Selecting key dimensions of the environment.
- All values were normalized with Min-Max scaling to fall within the value range of 0-1.

How to run the app

1. Install dependencies
``` bash
pip install dash plotly pandas

python interactivedietvisualizercorrectedFINAL.py
```

Go to your browser and navigate to the address http://127.0.0.1:8050.
