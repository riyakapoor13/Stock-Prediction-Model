import pandas as pd
import re
from textblob import TextBlob

# Load the dataset
reddit_data_path = "reddit_posts_extended.csv"  # Replace with your file path
reddit_df = pd.read_csv(reddit_data_path)

# Step 1: Clean the 'title' and 'body' columns
def clean_text(text):
    if pd.isna(text):
        return ""
    # Remove emojis, special characters, and extra whitespaces
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)  # Remove emojis
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespaces
    return text.lower()  # Convert to lowercase

reddit_df['title'] = reddit_df['title'].apply(clean_text)
reddit_df['body'] = reddit_df['body'].apply(clean_text)

# Combine 'title' and 'body' into a single column for analysis
reddit_df['text'] = reddit_df['title'] + " " + reddit_df['body']

# Step 2: Sentiment Analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity  # Polarity ranges from -1 (negative) to +1 (positive)
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

reddit_df['sentiment'] = reddit_df['text'].apply(get_sentiment)

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

reddit_df['stock_mentions'] = reddit_df['text'].apply(check_keywords)

# Step 4: Additional Features
reddit_df['post_length'] = reddit_df['text'].apply(len)  # Length of each post
reddit_df['has_url'] = reddit_df['body'].str.contains(r'https?://').astype(int)  # Check if post body contains a URL

# Save the enhanced dataset
enhanced_csv_path = "enhanced_reddit_data.csv"
reddit_df.to_csv(enhanced_csv_path, index=False)
print(f"Enhanced Reddit dataset saved to {enhanced_csv_path}")
