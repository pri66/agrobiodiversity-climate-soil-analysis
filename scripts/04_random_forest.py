# ============================================================
# RANDOM FOREST REGRESSION
# Agro-Biodiversity Project
# ============================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

# ============================================================
# LOAD DATA
# ============================================================

file = r"E:\AGC\outputs\Master_Dataset_Final.csv"

df = pd.read_csv(file)

print("="*70)
print("MASTER DATASET")
print("="*70)

print(df.shape)
print(df.head())

# ============================================================
# REMOVE UNUSED COLUMNS
# ============================================================

df = df.drop(columns=[
    "Row",
    "Col",
    "HWSD2_SMU_ID",
    "DRAINAGE"
])

# ============================================================
# REMOVE MISSING VALUES
# ============================================================

df = df.dropna()

print("\nDataset after cleaning")
print(df.shape)

# ============================================================
# TARGET VARIABLE
# ============================================================

y = df["Shannon"]

# ============================================================
# PREDICTORS
# ============================================================

X = df[[
    "BIO1",
    "BIO4",
    "BIO12",
    "BIO19",
    "SAND",
    "ORG_CARBON",
    "PH_WATER",
    "AWC"
]]

y = df["Shannon"]

print("\nPredictor Variables\n")
print(X.columns.tolist())

# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ============================================================
# PARAMETER GRID
# ============================================================

param_grid = {

    "n_estimators":[200,300,500],

    "max_depth":[3,5,None],

    "min_samples_split":[2,4],

    "min_samples_leaf":[1,2]

}

# ============================================================
# RANDOM FOREST
# ============================================================

rf = RandomForestRegressor(
    random_state=42,
    oob_score=True
)

grid = GridSearchCV(

    estimator=rf,

    param_grid=param_grid,

    cv=5,

    scoring="r2",

    n_jobs=-1

)

print("\nTraining Random Forest...")

grid.fit(X_train,y_train)

print("Done.")

# ============================================================
# BEST MODEL
# ============================================================

model = grid.best_estimator_
print("\nOut-of-Bag Score")

print(round(model.oob_score_,3))

print("\nBest Parameters\n")

print(grid.best_params_)

# ============================================================
# PREDICTIONS
# ============================================================

pred = model.predict(X_test)

# ============================================================
# METRICS
# ============================================================

r2 = r2_score(y_test,pred)

rmse = np.sqrt(mean_squared_error(y_test,pred))

mae = mean_absolute_error(y_test,pred)

print("\nModel Performance")

print("R2   :",round(r2,3))

print("RMSE :",round(rmse,3))

print("MAE  :",round(mae,3))

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importance = pd.DataFrame({

    "Feature":X.columns,

    "Importance":model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance\n")

print(importance)

# ============================================================
# SAVE OUTPUTS
# ============================================================

importance.to_csv(
    r"E:\AGC\outputs\Feature_Importance.csv",
    index=False
)

performance = pd.DataFrame({

    "R2":[r2],

    "RMSE":[rmse],

    "MAE":[mae]

})

performance.to_csv(
    r"E:\AGC\outputs\Model_Performance.csv",
    index=False
)

prediction = pd.DataFrame({

    "Observed":y_test,

    "Predicted":pred

})

prediction.to_csv(
    r"E:\AGC\outputs\Observed_vs_Predicted.csv",
    index=False
)

print("\nOutputs Saved Successfully")

import joblib

joblib.dump(
    model,
    r"E:\AGC\outputs\RandomForest_Final.pkl"
)

print("\nModel saved.")