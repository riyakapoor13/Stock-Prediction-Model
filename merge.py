import pandas as pd
import re
from datetime import datetime

# Step 1: Load the dataset
merged_data_path = "merged_stock_data.csv"  # Update with your file path
try:
    merged_df = pd.read_csv(merged_data_path)
except FileNotFoundError:
    print(f"File not found. Ensure that the file exists at: {merged_data_path}")
    raise

# Step 2: Data Cleaning
# Drop rows with missing 'text'
cleaned_df = merged_df.dropna(subset=['text'])

# Remove duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Step 3: Handle Timestamp Parsing
# Define a function to parse multiple timestamp formats
def parse_timestamp(timestamp):
    try:
        # Attempt to parse the timestamp using flexible formats
        return pd.to_datetime(timestamp, errors='coerce')  # Errors will result in NaT
    except Exception as e:
        print(f"Error parsing timestamp: {timestamp}")
        return None

# Apply the parsing function to the 'timestamp' column
cleaned_df['timestamp'] = cleaned_df['timestamp'].apply(parse_timestamp)

# Drop rows with invalid timestamps
cleaned_df = cleaned_df.dropna(subset=['timestamp'])

# Step 4: Temporal Feature Engineering
# Extract time-based features
cleaned_df['hour_of_day'] = cleaned_df['timestamp'].dt.hour  # Hour of the day
cleaned_df['day_of_week'] = cleaned_df['timestamp'].dt.day_name()  # Day of the week
cleaned_df['is_market_open'] = cleaned_df['hour_of_day'].apply(lambda x: 1 if 9 <= x <= 15 else 0)  # Market open hours (9 AM to 3 PM)

# Step 5: Advanced Stock Mentions Detection
keywords = [
    "reliance", "tcs", "infosys", "hdfc", "icici", "sbi", "adani", "sensex", "nifty",
    "bse", "midcap", "largecap", "smallcap", "nifty50", "bullish", "bearish", "ipo",
    "dividends", "buybacks", "earnings", "stock split", "mutual funds", "fii", "dii",
    "inflation", "interest rates", "rate hikes"
]

def check_keywords(text):
    mentioned_keywords = [keyword for keyword in keywords if keyword in text.lower()]
    return ", ".join(mentioned_keywords) if mentioned_keywords else "None"

cleaned_df['stock_mentions'] = cleaned_df['text'].apply(check_keywords)

# Step 6: Sentiment Refinement
from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity  # Polarity ranges from -1 (negative) to +1 (positive)
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

cleaned_df['sentiment'] = cleaned_df['text'].apply(get_sentiment)

# Step 7: Save the Enhanced Dataset
enhanced_csv_path = "enhanced_merged_stock_data.csv"
cleaned_df.to_csv(enhanced_csv_path, index=False)
print(f"Enhanced dataset saved to {enhanced_csv_path}")
