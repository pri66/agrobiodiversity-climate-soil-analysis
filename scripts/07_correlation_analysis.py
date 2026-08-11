import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read correlation matrix
corr = pd.read_csv(
    r"E:\AGC\outputs\Correlation_Matrix.csv",
    index_col=0
)

# Figure size
plt.figure(figsize=(10, 8))

# Heatmap
ax = sns.heatmap(
    corr,
    annot=True,              # Show values
    fmt=".2f",               # Two decimal places
    cmap="coolwarm",         # Blue-White-Red
    center=0,
    vmin=-1,
    vmax=1,
    linewidths=0.6,
    linecolor="white",
    square=True,
    cbar_kws={
        "label": "Pearson Correlation Coefficient",
        "shrink": 0.85
    }
)

# Title
plt.title(
    "Correlation Matrix of Biodiversity and Climate Variables",
    fontsize=18,
    fontweight="bold",
    pad=18
)

# Axis labels
plt.xticks(
    rotation=45,
    ha="right",
    fontsize=12
)

plt.yticks(
    rotation=0,
    fontsize=12
)

# Colorbar
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=11)
cbar.set_label(
    "Pearson Correlation Coefficient",
    fontsize=12
)

plt.tight_layout()

# Save
plt.savefig(
    r"E:\AGC\outputs\Figure_06_Correlation_Heatmap.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()