import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Feature-Engineered Dataset ---
daily_data_path = "featen_daily_data.csv"
daily_df = pd.read_csv(daily_data_path)

# --- Define Features and Target ---
features = ['total_mentions', 'rolling_mentions_3', 'rolling_sentiment_3', 'lagged_mentions', 'lagged_sentiment']
target = 'sentiment_ratio'

# Check and handle missing values
if daily_df[features].isnull().sum().sum() > 0:
    print("Missing values found. Filling with mean...")
    daily_df[features] = daily_df[features].fillna(daily_df[features].mean())

# Split the data into features (X) and target (y)
X = daily_df[features]
y = daily_df[target]

# --- Data Splitting ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Train the LightGBM Regressor ---
print("Training LightGBM Regressor...")
lgb_model = LGBMRegressor(
    n_estimators=500,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
lgb_model.fit(X_train, y_train)

# --- Predictions ---
y_pred = lgb_model.predict(X_test)

# --- Evaluation Metrics ---
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation Metrics ---")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared (R²): {r2:.4f}")

# --- Feature Importance ---
print("\nFeature Importance:")
feature_importances = lgb_model.feature_importances_
for feature, importance in zip(features, feature_importances):
    print(f"{feature}: {importance:.4f}")

# Plot Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x=features, y=feature_importances, palette="viridis")
plt.title("Feature Importance (LightGBM)")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()

# --- Residual Analysis ---
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, bins=30, color='blue')
plt.title("Residual Distribution")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(y_test, residuals, alpha=0.5)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs. True Values")
plt.xlabel("True Values")
plt.ylabel("Residuals")
plt.show()

# --- Save Model and Predictions ---
# Save predictions to a CSV file
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
predictions_df.to_csv("lightgbm_daily_predictions.csv", index=False)
print("\nPredictions saved to 'lightgbm_daily_predictions.csv'!")
