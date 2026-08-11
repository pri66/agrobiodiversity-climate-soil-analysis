"""
==============================================================
Figure 08
SHAP Feature Importance & Summary Plot

Project:
Agro-Biodiversity Assessment using Climate and Soil Variables

Author:
Praveen

Description:
Generates publication-quality SHAP Feature Importance
and SHAP Summary plots for the optimized Random Forest model.

Outputs

Figure_08A_SHAP_Bar.png
Figure_08B_SHAP_Summary.png

==============================================================
"""
import os
import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt
figure_folder = r"E:\AGC\outputs\Figures"

os.makedirs(
    figure_folder,
    exist_ok=True
)
print("="*60)
print("Loading dataset...")
print("="*60)

df = pd.read_csv(
    r"E:\AGC\outputs\Master_Dataset_Final.csv"
)
df = df.drop(
    columns=[
        "Row",
        "Col",
        "HWSD2_SMU_ID",
        "DRAINAGE"
    ]
)

df = df.dropna()
predictors = [

    "BIO1",

    "BIO4",

    "BIO12",

    "BIO19",

    "SAND",

    "ORG_CARBON",

    "PH_WATER",

    "AWC"

]

X = df[predictors]
X.columns = [
    "Annual Mean Temp.",
    "Temp. Seasonality",
    "Annual Precipitation",
    "Precipitation (Coldest Qtr.)",
    "Sand Content",
    "Organic Carbon",
    "Soil pH",
    "Available Water Capacity"
]
print()

print("Loading Random Forest model...")

model = joblib.load(
    r"E:\AGC\outputs\RandomForest_Final.pkl"
)
print()

print("Calculating SHAP values...")

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)
# ============================================================
# Publication Style
# ============================================================

plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 13
plt.rcParams["xtick.labelsize"] = 11
plt.rcParams["ytick.labelsize"] = 11

# ============================================================
# Figure 08A
# SHAP Feature Importance (Bar Plot)
# ============================================================

print()
print("=" * 60)
print("Creating Figure 08A - SHAP Feature Importance")
print("=" * 60)

plt.figure(figsize=(10, 7))

shap.summary_plot(
    shap_values,
    X,
    plot_type="bar",
    show=False,
    color="#2E8B57"
)

plt.title(
    "SHAP Feature Importance",
    fontsize=18,
    fontweight="bold",
    pad=15
)

plt.xlabel(
    "Mean Absolute SHAP Value",
    fontsize=13,
    fontweight="bold"
)

plt.ylabel("")

plt.tight_layout()

bar_output = os.path.join(
    figure_folder,
    "Figure_08A_SHAP_Bar.png"
)

plt.savefig(
    bar_output,
    dpi=600,
    bbox_inches="tight"
)

plt.close()

print("Saved:")
print(bar_output)

# ============================================================
# Figure 08B
# SHAP Summary Plot (Beeswarm)
# ============================================================

print()
print("=" * 60)
print("Creating Figure 08B - SHAP Summary")
print("=" * 60)

plt.figure(figsize=(11, 7))

shap.summary_plot(
    shap_values,
    X,
    show=False
)

plt.title(
    "SHAP Summary Plot Explaining Random Forest Predictions",
    fontsize=18,
    fontweight="bold",
    pad=18
)

plt.xlabel(
    "SHAP Value (Impact on Model Output)",
    fontsize=13,
    fontweight="bold"
)

plt.tight_layout()

summary_output = os.path.join(
    figure_folder,
    "Figure_08B_SHAP_Summary.png"
)

plt.savefig(
    summary_output,
    dpi=600,
    bbox_inches="tight"
)

plt.close()

print("Saved:")
print(summary_output)

# ============================================================
# Completed
# ============================================================

print()
print("=" * 60)
print("SHAP ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print()
print("Generated Figures")
print("-------------------------------")
print("Figure_08A_SHAP_Bar.png")
print("Figure_08B_SHAP_Summary.png")