import pandas as pd
import re
from textblob import TextBlob

# Load the dataset
telegram_data_path = "telegram_group_messages.csv"  # Replace with your file path
telegram_df = pd.read_csv(telegram_data_path)

# Step 1: Convert 'date' to datetime format
telegram_df['date'] = pd.to_datetime(telegram_df['date'])

# Step 2: Clean the 'text' column
def clean_text(text):
    # Remove emojis, special characters, and extra whitespaces
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)  # Remove emojis
    text = re.sub(r'\*\*|\n|\r', ' ', text)  # Remove special characters like **, newlines
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespaces
    return text.lower()  # Convert to lowercase

telegram_df['text'] = telegram_df['text'].apply(clean_text)

# Step 3: Sentiment Analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity  # Polarity ranges from -1 (negative) to +1 (positive)
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

telegram_df['sentiment'] = telegram_df['text'].apply(get_sentiment)

# Step 4: Expanded Keyword Extraction - Check for Stock Mentions
keywords = [
    "reliance", "tcs", "infosys", "hdfc bank", "icici bank", "sbi", "adani", "itc", "l&t", "wipro",
    "hcl", "titan", "ntpc", "axis bank", "bajaj finance", "maruti", "tata motors", "hindustan unilever",
    "sun pharma", "power grid", "coal india", "sensex", "nifty50", "nse", "bse", "midcap", "largecap",
    "smallcap", "niftybank", "s&p", "stock market", "bullish", "bearish", "ipo", "banking stocks",
    "it stocks", "energy stocks", "auto stocks", "oil stocks", "psu stocks", "inflation", "interest rates",
    "rate hikes", "dividends", "buybacks", "mutual funds", "fii", "dii", "earnings", "stock split"
]

def check_keywords(text):
    mentioned_keywords = [keyword for keyword in keywords if keyword in text]
    return ", ".join(mentioned_keywords) if mentioned_keywords else "None"

telegram_df['stock_mentions'] = telegram_df['text'].apply(check_keywords)

# Step 5: Additional Features
telegram_df['message_length'] = telegram_df['text'].apply(len)  # Length of each message
telegram_df['has_url'] = telegram_df['text'].str.contains(r'https?://').astype(int)  # Check if message contains a URL

# Save the enhanced dataset
enhanced_csv_path = "enhanced_telegram_data_extended.csv"
telegram_df.to_csv(enhanced_csv_path, index=False)
print(f"Enhanced Telegram dataset saved to {enhanced_csv_path}")
