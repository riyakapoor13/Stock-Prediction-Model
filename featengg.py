import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the processed datasets
hourly_data_path = "hourly_aggregated_data_v2.csv"
daily_data_path = "daily_aggregated_data_v2.csv"

hourly_df = pd.read_csv(hourly_data_path)
daily_df = pd.read_csv(daily_data_path)

# Convert timestamp and date columns to datetime
hourly_df['hour'] = pd.to_datetime(hourly_df['hour'])
daily_df['date'] = pd.to_datetime(daily_df['date'])

# --- 1. Temporal Features ---
# Hourly Data: Extract hour of day
hourly_df['hour_of_day'] = hourly_df['hour'].dt.hour
hourly_df['is_market_open'] = hourly_df['hour_of_day'].apply(lambda x: 1 if 9 <= x <= 15 else 0)

# Daily Data: Extract day of week
daily_df['day_of_week'] = daily_df['date'].dt.day_name()

# --- 2. Lagging Features ---
# Daily Data: Create rolling averages and lagged features
daily_df['rolling_mentions_3'] = daily_df['total_mentions'].rolling(window=3, min_periods=1).mean()
daily_df['rolling_sentiment_3'] = daily_df['sentiment_ratio'].rolling(window=3, min_periods=1).mean()
daily_df['lagged_mentions'] = daily_df['total_mentions'].shift(1)
daily_df['lagged_sentiment'] = daily_df['sentiment_ratio'].shift(1)

# Hourly Data: Create rolling averages
hourly_df['rolling_mentions_3h'] = hourly_df['total_mentions'].rolling(window=3, min_periods=1).mean()
hourly_df['rolling_sentiment_3h'] = hourly_df['sentiment_ratio'].rolling(window=3, min_periods=1).mean()

# --- 3. Normalize Numeric Features ---
scaler = MinMaxScaler()
numeric_features_daily = ['total_mentions', 'sentiment_ratio', 'rolling_mentions_3', 'rolling_sentiment_3']
numeric_features_hourly = ['total_mentions', 'sentiment_ratio', 'rolling_mentions_3h', 'rolling_sentiment_3h']

daily_df[numeric_features_daily] = scaler.fit_transform(daily_df[numeric_features_daily])
hourly_df[numeric_features_hourly] = scaler.fit_transform(hourly_df[numeric_features_hourly])

# Save the enhanced datasets
hourly_df.to_csv("featen_hourly_data.csv", index=False)
daily_df.to_csv("featen_daily_data.csv", index=False)

print("Feature engineering completed. Enhanced datasets saved!")
