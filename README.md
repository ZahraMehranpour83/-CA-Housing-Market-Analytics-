# -CA-Housing-Market-Analytics-
# California Housing Data Analysis

This project includes analysis and visualization of housing price data in California, retrieved from the OpenML dataset with ID `43705`.

## Features

- Load data from OpenML
- Encode categorical variables using `LabelEncoder`
- Visualize data using:
  - Streamlit and Plotly (`home_c.py`)
  - Seaborn and Matplotlib (`plot.py`)
- Compare average house prices based on features like `ocean_proximity` and `population`

## Files

- `home_c.py`: An interactive Streamlit interface to select features and display charts
- `plot.py`: Statistical visualization using Seaborn

## Running the Streamlit App

To launch the Streamlit UI:

```bash
streamlit run home_c.py
