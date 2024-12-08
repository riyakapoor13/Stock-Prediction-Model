import pandas as pd
import numpy as np

# Load the enhanced datasets
telegram_path = "enhanced_telegram_data_extended.csv"
twitter_path = "enhanced_twitter_data.csv"
reddit_path = "enhanced_reddit_data.csv"

telegram_df = pd.read_csv(telegram_path)
twitter_df = pd.read_csv(twitter_path)
reddit_df = pd.read_csv(reddit_path)

# --- 1. Clean and Normalize Data ---
# Ensure timestamps are in datetime format
for df in [telegram_df, twitter_df, reddit_df]:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Normalize sentiment labels
for df in [telegram_df, twitter_df, reddit_df]:
    df['sentiment'] = df['sentiment'].str.lower()

# --- 2. Feature Engineering ---
# Example: Add rolling averages (7-day rolling window for Twitter data)
twitter_df['rolling_mentions'] = twitter_df['stock_mentions'].rolling(window=7, min_periods=1).mean()
twitter_df['rolling_sentiment_ratio'] = twitter_df['sentiment_ratio'].rolling(window=7, min_periods=1).mean()

# Add a 'day_of_week' feature
for df in [telegram_df, twitter_df, reddit_df]:
    df['day_of_week'] = df['timestamp'].dt.day_name()

# Add market session mapping
for df in [telegram_df, twitter_df, reddit_df]:
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['is_market_open'] = df['hour_of_day'].apply(lambda x: 1 if 9 <= x <= 15 else 0)

# --- 3. Merge Datasets ---
# Merge all datasets based on timestamp
merged_df = pd.concat([telegram_df, twitter_df, reddit_df], axis=0)

# --- 4. Handle Missing Values ---
# Forward fill missing values for continuous features
merged_df.fillna(method='ffill', inplace=True)

# Replace missing categorical values with "unknown"
merged_df.fillna('unknown', inplace=True)

# --- 5. Normalize and Scale Numeric Features ---
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
numeric_features = ['stock_mentions', 'sentiment_ratio', 'rolling_mentions', 'rolling_sentiment_ratio']
merged_df[numeric_features] = scaler.fit_transform(merged_df[numeric_features])

# --- 6. Save the Processed Dataset ---
merged_path = "processed_stock_data.csv"
merged_df.to_csv(merged_path, index=False)

print(f"Processed dataset saved to {merged_path}")
