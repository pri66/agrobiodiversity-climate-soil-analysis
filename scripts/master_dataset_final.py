# ============================================================
# AGRO-BIODIVERSITY INDICES
# Calculates Shannon, Simpson and Evenness together
# ============================================================

import numpy as np
import rasterio
from pathlib import Path

# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------

crop_folder = Path(r"E:\AGC\Data\crop\clipped")

shannon_file = r"E:\AGC\outputs\Shannon_Diversity.tif"
simpson_file = r"E:\AGC\outputs\Simpson_Diversity.tif"
evenness_file = r"E:\AGC\outputs\Evenness_Index.tif"

# ------------------------------------------------------------
# LOAD RASTERS
# ------------------------------------------------------------

crop_files = sorted(crop_folder.glob("*.tif"))

print("Crop rasters:", len(crop_files))

rasters = []

profile = None

for i, file in enumerate(crop_files):

    with rasterio.open(file) as src:

        if i == 0:
            profile = src.profile.copy()

        arr = src.read(1).astype(np.float32)

        if src.nodata is not None:
            arr[arr == src.nodata] = np.nan

        rasters.append(arr)

stack = np.stack(rasters)

layers, rows, cols = stack.shape

print("Raster size:", rows, "x", cols)

# ------------------------------------------------------------
# OUTPUT ARRAYS
# ------------------------------------------------------------

shannon = np.full((rows, cols), np.nan, dtype=np.float32)
simpson = np.full((rows, cols), np.nan, dtype=np.float32)
evenness = np.full((rows, cols), np.nan, dtype=np.float32)

# ------------------------------------------------------------
# CALCULATE
# ------------------------------------------------------------

for row in range(rows):

    for col in range(cols):

        pixel = stack[:, row, col]

        pixel = pixel[~np.isnan(pixel)]

        pixel = pixel[pixel > 0]

        if len(pixel) == 0:
            continue

        total = pixel.sum()

        if total <= 0:
            continue

        p = pixel / total

        # Shannon
        H = -np.sum(p * np.log(p))

        # Simpson
        D = 1 - np.sum(p ** 2)

        # Evenness
        S = len(pixel)

        if S > 1:
            E = H / np.log(S)
        else:
            E = np.nan

        shannon[row, col] = H
        simpson[row, col] = D
        evenness[row, col] = E

# ------------------------------------------------------------
# SAVE
# ------------------------------------------------------------

profile.update(
    dtype=rasterio.float32,
    count=1,
    nodata=np.nan
)

with rasterio.open(shannon_file, "w", **profile) as dst:
    dst.write(shannon, 1)

with rasterio.open(simpson_file, "w", **profile) as dst:
    dst.write(simpson, 1)

with rasterio.open(evenness_file, "w", **profile) as dst:
    dst.write(evenness, 1)

# ------------------------------------------------------------
# STATISTICS
# ------------------------------------------------------------

print("\n============================")
print("SHANNON")
print("============================")
print("Min :", np.nanmin(shannon))
print("Max :", np.nanmax(shannon))
print("Mean:", np.nanmean(shannon))

print("\n============================")
print("SIMPSON")
print("============================")
print("Min :", np.nanmin(simpson))
print("Max :", np.nanmax(simpson))
print("Mean:", np.nanmean(simpson))

print("\n============================")
print("EVENNESS")
print("============================")
print("Min :", np.nanmin(evenness))
print("Max :", np.nanmax(evenness))
print("Mean:", np.nanmean(evenness))

print("\nFinished.")