import pandas as pd
import re
from textblob import TextBlob

# Load the dataset
twitter_data_path = "indian_stock_tweets.csv"  # Replace with your file path
twitter_df = pd.read_csv(twitter_data_path)

# Step 1: Clean the 'text' column
def clean_text(text):
    # Remove emojis, special characters, and extra whitespaces
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)  # Remove emojis
    text = re.sub(r'RT\s+', '', text)  # Remove Retweet (RT)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s#@]', '', text)  # Remove special characters except # and @
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespaces
    return text.lower()  # Convert to lowercase

twitter_df['text'] = twitter_df['text'].apply(clean_text)

# Step 2: Sentiment Analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity  # Polarity ranges from -1 (negative) to +1 (positive)
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

twitter_df['sentiment'] = twitter_df['text'].apply(get_sentiment)

# Step 3: Keyword Matching - Check for Stock Mentions
keywords = [
    "reliance", "tcs", "infosys", "hdfc", "icici", "sbi", "adani", "sensex", "nifty",
    "bse", "midcap", "largecap", "smallcap", "nifty50", "bullish", "bearish", "ipo",
    "dividends", "buybacks", "earnings", "stock split", "mutual funds", "fii", "dii",
    "inflation", "interest rates", "rate hikes"
]

def check_keywords(text):
    mentioned_keywords = [keyword for keyword in keywords if keyword in text]
    return ", ".join(mentioned_keywords) if mentioned_keywords else "None"

twitter_df['stock_mentions'] = twitter_df['text'].apply(check_keywords)

# Step 4: Hashtag Extraction
def extract_hashtags(text):
    hashtags = re.findall(r"#(\w+)", text)  # Extract words starting with #
    return ", ".join(hashtags) if hashtags else "None"

twitter_df['hashtags'] = twitter_df['text'].apply(extract_hashtags)

# Step 5: Additional Features
twitter_df['tweet_length'] = twitter_df['text'].apply(len)  # Length of each tweet
twitter_df['has_url'] = twitter_df['text'].str.contains(r'https?://').astype(int)  # Check if tweet contains a URL

# Save the enhanced dataset
enhanced_csv_path = "enhanced_twitter_data.csv"
twitter_df.to_csv(enhanced_csv_path, index=False)
print(f"Enhanced Twitter dataset saved to {enhanced_csv_path}")
