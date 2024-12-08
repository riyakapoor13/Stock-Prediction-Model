import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
hourly_data_path = "/Users/pancakes/Desktop/task/hourly_aggregated_data_v2.csv"
daily_data_path = "/Users/pancakes/Desktop/task/daily_aggregated_data_v2.csv"

hourly_df = pd.read_csv(hourly_data_path)
daily_df = pd.read_csv(daily_data_path)

# Convert timestamp and date columns to datetime
hourly_df['hour'] = pd.to_datetime(hourly_df['hour'])
daily_df['date'] = pd.to_datetime(daily_df['date'])

# --- 1. Summary Statistics ---
print("Hourly Data Summary:")
print(hourly_df.describe())

print("\nDaily Data Summary:")
print(daily_df.describe())

# --- 2. Missing Values ---
print("\nMissing Values in Hourly Data:")
print(hourly_df.isnull().sum())

print("\nMissing Values in Daily Data:")
print(daily_df.isnull().sum())

# --- 3. Visualize Trends Over Time ---
# Hourly Trends
plt.figure(figsize=(12, 6))
plt.plot(hourly_df['hour'], hourly_df['total_mentions'], label='Total Mentions')
plt.plot(hourly_df['hour'], hourly_df['sentiment_ratio'], label='Sentiment Ratio')
plt.title("Hourly Trends in Mentions and Sentiment Ratio")
plt.xlabel("Time (Hourly)")
plt.ylabel("Values")
plt.legend()
plt.grid()
plt.show()

# Daily Trends
plt.figure(figsize=(12, 6))
plt.plot(daily_df['date'], daily_df['total_mentions'], label='Total Mentions')
plt.plot(daily_df['date'], daily_df['sentiment_ratio'], label='Sentiment Ratio')
plt.title("Daily Trends in Mentions and Sentiment Ratio")
plt.xlabel("Date")
plt.ylabel("Values")
plt.legend()
plt.grid()
plt.show()

# --- 4. Correlation Matrix ---
plt.figure(figsize=(10, 6))
sns.heatmap(daily_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix - Daily Data")
plt.show()

# --- 5. Time-Based Analysis ---
# Hourly Analysis
hourly_df['hour_of_day'] = hourly_df['hour'].dt.hour
hourly_mentions_by_hour = hourly_df.groupby('hour_of_day')['total_mentions'].mean()

plt.figure(figsize=(10, 6))
hourly_mentions_by_hour.plot(kind='bar', color='skyblue')
plt.title("Average Mentions by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Average Mentions")
plt.xticks(rotation=0)
plt.grid()
plt.show()

# Daily Analysis
daily_df['day_of_week'] = daily_df['date'].dt.day_name()
daily_mentions_by_day = daily_df.groupby('day_of_week')['total_mentions'].mean()

plt.figure(figsize=(10, 6))
daily_mentions_by_day.plot(kind='bar', color='orange')
plt.title("Average Mentions by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Average Mentions")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# --- 6. Outlier Detection ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=daily_df[['total_mentions', 'sentiment_ratio']])
plt.title("Outlier Detection for Mentions and Sentiment Ratio")
plt.show()
