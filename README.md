#  Agrobiodiversity Assessment Using Climate, Soil, GIS and Machine Learning

### A geospatial machine learning project integrating GIS, climate variables, soil properties, Random Forest regression, and SHAP explainability to investigate spatial patterns of agrobiodiversity in Jabalpur District, Madhya Pradesh, India.

## Project Overview

Agrobiodiversity plays a crucial role in maintaining resilient agricultural ecosystems and supporting sustainable food production. Climate conditions and soil characteristics are among the primary environmental factors influencing biodiversity patterns across landscapes.

This project investigates the relationship between climate variables, soil properties, and agrobiodiversity in **Jabalpur District, Madhya Pradesh, India** using Geographic Information Systems (GIS) and Machine Learning techniques.

The workflow integrates spatial datasets, climate variables from WorldClim, soil information from the Harmonized World Soil Database (HWSD), and biodiversity indices derived from crop distribution. A Random Forest regression model was developed to predict the Shannon Diversity Index, while SHAP (SHapley Additive exPlanations) was used to interpret the contribution of individual environmental variables to model predictions.

The project demonstrates an end-to-end geospatial machine learning workflow, including data preparation, spatial analysis, exploratory data analysis, predictive modelling, and model interpretation.

## Project Objectives

The main objectives of this project are:

- Assess spatial patterns of agrobiodiversity in Jabalpur District using the Shannon Diversity Index.
- Investigate the influence of climate and soil variables on agrobiodiversity.
- Develop a Random Forest regression model to predict agrobiodiversity.
- Interpret model predictions using SHAP (SHapley Additive exPlanations).
- Produce publication-quality maps and visualizations using GIS and Python.
- Demonstrate a complete geospatial machine learning workflow suitable for environmental research.

## Project Workflow

The overall workflow of this project is illustrated below:

1. Data Collection
   - Climate data (WorldClim Bioclimatic Variables)
   - Soil data (HWSD)
   - Crop distribution datasets

2. Data Preparation
   - Raster clipping
   - Coordinate system alignment
   - Soil property extraction
   - Biodiversity index calculation

3. Exploratory Data Analysis
   - Correlation analysis
   - Statistical summaries
   - Multicollinearity assessment

4. Machine Learning
   - Random Forest Regression
   - Hyperparameter tuning
   - Model evaluation

5. Model Interpretation
   - Feature Importance
   - SHAP Summary Plot
   - SHAP Dependence Plots

6. Visualization
   - Study Area Map
   - Climate Maps
   - Soil Maps
   - Statistical Figures

## Datasets

The following datasets were used in this project:

| Dataset | Source | Purpose |
|----------|--------|---------|
| WorldClim Version 2.1 | https://www.worldclim.org/ | Bioclimatic variables |
| Harmonized World Soil Database (HWSD v2.0) | https://gaez.fao.org/pages/hwsd | Soil properties |
| Crop Distribution Dataset | SPAM 2020 / Project dataset | Agrobiodiversity estimation |
| Administrative Boundary | Survey of India / Open Government Data | Study area boundary |

### Climate Variables Used

- BIO1 – Annual Mean Temperature
- BIO4 – Temperature Seasonality
- BIO12 – Annual Precipitation
- BIO19 – Precipitation of Coldest Quarter

### Soil Variables Used

- Sand Content
- Organic Carbon
- Soil pH
- Available Water Capacity (AWC)

## Software & Tools

### GIS Software
- QGIS 3.x

### Programming Language
- Python 3.12

### Python Libraries
- pandas
- numpy
- rasterio
- geopandas
- matplotlib
- scikit-learn
- shap
- joblib

### Machine Learning
- Random Forest Regression
- GridSearchCV
- SHAP (SHapley Additive Explanations)

### Development Environment
- Visual Studio Code
- Jupyter Notebook (for exploratory analysis)

### Version Control
- Git
- GitHub

## Project Structure

```
agrobiodiversity-climate-soil-analysis/
│
├── data/
│   └── Master_Dataset_Final.csv
│
├── docs/
│
├── figures/
│   ├── Figure_01_Study_Area.png
│   ├── Figure_02_BIO1_Annual_Mean_Temperature.png
│   ├── Figure_03_BIO4_Temperature_Seasonality.png
│   ├── Figure_04_BIO12_Annual_Precipitation.png
│   ├── Figure_05_BIO19_Precipitation_Coldest_Quarter.png
│   ├── Figure_06_HWSD2_Soil_Map.png
│   ├── Figure_07_Correlation_Heatmap.png
│   ├── Figure_08_SHAP_Summary.png
│   ├── Figure_09_SHAP_BIO12.png
│   ├── Figure_10_SHAP_BIO4.png
│   ├── Figure_11_SHAP_BIO1.png
│   └── Figure_12_SHAP_BIO19.png
│
├── outputs/
│   ├── Feature_Importance.csv
│   ├── Model_Performance.csv
│   ├── Observed_vs_Predicted.csv
│   ├── Correlation_Matrix.csv
│   └── RandomForest_Final.pkl
│
├── scripts/
│
├── README.md
└── LICENSE
```

## Study Area

The study was conducted in **Jabalpur District, Madhya Pradesh, India**.

<p align="center">
  <img src="figures/Figure_01_Study_Area.png" width="700">
</p>

**Figure 1.** Location of the study area showing Jabalpur District within Madhya Pradesh, India.
