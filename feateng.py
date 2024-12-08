import pandas as pd

# Load the enhanced dataset
enhanced_data_path = "/Users/pancakes/Desktop/task/enhanced/enhanced_merged_stock_data.csv"  # Replace with your file path
enhanced_df = pd.read_csv(enhanced_data_path)

# Ensure 'timestamp' is in datetime format
enhanced_df['timestamp'] = pd.to_datetime(enhanced_df['timestamp'], errors='coerce')

# Create explicit date and hour columns
enhanced_df['date'] = enhanced_df['timestamp'].dt.date
enhanced_df['hour'] = enhanced_df['timestamp'].dt.hour

# --- 1. Daily Aggregation ---
daily_aggregated = enhanced_df.groupby('date').agg(
    total_mentions=('stock_mentions', 'count'),
    positive_sentiment=('sentiment', lambda x: (x == 'Positive').sum()),
    negative_sentiment=('sentiment', lambda x: (x == 'Negative').sum()),
    neutral_sentiment=('sentiment', lambda x: (x == 'Neutral').sum())
)
daily_aggregated['sentiment_ratio'] = daily_aggregated['positive_sentiment'] / daily_aggregated['negative_sentiment'].replace(0, 1)
daily_aggregated['day_of_week'] = pd.to_datetime(daily_aggregated.index).day_name()

# --- 2. Hourly Aggregation ---
hourly_aggregated = enhanced_df.groupby(['date', 'hour']).agg(
    total_mentions=('stock_mentions', 'count'),
    positive_sentiment=('sentiment', lambda x: (x == 'Positive').sum()),
    negative_sentiment=('sentiment', lambda x: (x == 'Negative').sum()),
    neutral_sentiment=('sentiment', lambda x: (x == 'Neutral').sum())
)
hourly_aggregated['sentiment_ratio'] = hourly_aggregated['positive_sentiment'] / hourly_aggregated['negative_sentiment'].replace(0, 1)
hourly_aggregated['is_market_open'] = hourly_aggregated.index.get_level_values('hour').map(lambda x: 1 if 9 <= x <= 15 else 0)

# --- 3. Save the Processed Datasets ---
hourly_aggregated_path = "hourly_aggregated_data_v2.csv"
daily_aggregated_path = "daily_aggregated_data_v2.csv"

daily_aggregated.to_csv(daily_aggregated_path, index=True)
hourly_aggregated.to_csv(hourly_aggregated_path, index=True)

print(f"Daily aggregated data saved to {daily_aggregated_path}")
print(f"Hourly aggregated data saved to {hourly_aggregated_path}")
