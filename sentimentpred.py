import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load the feature-engineered dataset
daily_data_path = "featen_daily_data.csv"
hourly_data_path = "featen_hourly_data.csv"

daily_df = pd.read_csv(daily_data_path)

# Define features and target
features = ['total_mentions', 'rolling_mentions_3', 'rolling_sentiment_3', 'lagged_mentions', 'lagged_sentiment']
target = 'sentiment_ratio'

# Discretize the target into classes (for classification)
daily_df['target'] = pd.cut(daily_df[target], bins=[-float('inf'), 0.5, 1.5, float('inf')], labels=['Negative', 'Neutral', 'Positive'])

# Split the data into training and testing sets
X = daily_df[features]
y = daily_df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Plot confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Neutral', 'Positive'], yticklabels=['Negative', 'Neutral', 'Positive'])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Feature Importance
feature_importances = clf.feature_importances_
plt.figure(figsize=(10, 6))
sns.barplot(x=features, y=feature_importances)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()
