import pandas as pd
import matplotlib.pyplot as plt

# Load the enhanced dataset
enhanced_data_path = "enhanced_merged_stock_data.csv"  # Update this to your file path
enhanced_df = pd.read_csv(enhanced_data_path)

# Ensure 'timestamp' is in datetime format
enhanced_df['timestamp'] = pd.to_datetime(enhanced_df['timestamp'])

# --- 1. Sentiment Distribution ---
sentiment_counts = enhanced_df['sentiment'].value_counts()
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color='orange')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Frequency")
plt.show()

# --- 2. Top Mentioned Stocks ---
top_stocks = enhanced_df['stock_mentions'].str.split(', ').explode().value_counts().head(10)
plt.figure(figsize=(10, 6))
top_stocks.plot(kind='bar', color='orange')
plt.title("Top 10 Most Mentioned Stocks")
plt.xlabel("Stock")
plt.ylabel("Mentions")
plt.show()

# --- 3. Sentiment Trends Over Time ---
sentiment_trend = enhanced_df.groupby(enhanced_df['timestamp'].dt.date)['sentiment'].value_counts().unstack().fillna(0)
plt.figure(figsize=(12, 6))
sentiment_trend.plot(title="Sentiment Trends Over Time", xlabel="Date", ylabel="Count", figsize=(12, 6))
plt.show()

# --- 4. Stock Mentions by Day ---
stock_mentions_daily = enhanced_df.groupby(enhanced_df['timestamp'].dt.date)['stock_mentions'].count()
plt.figure(figsize=(12, 6))
stock_mentions_daily.plot(kind='line', color='green')
plt.title("Stock Mentions Over Time")
plt.xlabel("Date")
plt.ylabel("Mentions")
plt.grid(True)
plt.show()

# --- 5. Positive vs Negative Sentiment Ratio ---
sentiment_ratio = enhanced_df.groupby(enhanced_df['timestamp'].dt.date)['sentiment'].apply(
    lambda x: (x == 'Positive').sum() / max((x == 'Negative').sum(), 1)  # Avoid division by zero
)
plt.figure(figsize=(12, 6))
sentiment_ratio.plot(kind='line', color='purple')
plt.title("Positive to Negative Sentiment Ratio Over Time")
plt.xlabel("Date")
plt.ylabel("Ratio")
plt.grid(True)
plt.show()

# --- 6. Mentions vs Sentiment Comparison ---
daily_mentions = enhanced_df.groupby(enhanced_df['timestamp'].dt.date)['stock_mentions'].count()
daily_sentiments = enhanced_df.groupby(enhanced_df['timestamp'].dt.date)['sentiment'].value_counts().unstack().fillna(0)

plt.figure(figsize=(12, 6))
plt.plot(daily_mentions.index, daily_mentions, label="Stock Mentions", color='blue')
plt.plot(daily_sentiments.index, daily_sentiments['Positive'], label="Positive Sentiment", color='green')
plt.plot(daily_sentiments.index, daily_sentiments['Negative'], label="Negative Sentiment", color='red')
plt.legend()
plt.title("Stock Mentions vs Sentiment Trends")
plt.xlabel("Date")
plt.ylabel("Count")
plt.grid(True)
plt.show()
