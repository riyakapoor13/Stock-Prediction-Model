import tweepy
import pandas as pd

# Replace with your keys and tokens
api_key = "Llm4AmbvtCe47QfGC8muYjhRX"
api_key_secret = "Y352EJOiiZR3uZoFIRfN8VneMSiXonirKnbrxhCGZWJIhWptd2"
access_token = "1865357447105519616-IwEDixILE2VaVS5avwL2WxDKOWDdc6"
access_token_secret = "EVHLbVRz9EFiaCzlfrocbD1A33RvC7ZPxBDe1xcYdP7oV"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAKOlxQEAAAAAejl3mZUe2BkCWLoT0ic90%2Bb0IAk%3DTHAV73GhJ6ofgBiriCHOXkFTN1peASRHxkeTUZbnIAH7nhTsWa"  # You need the Bearer Token for API v2

# Authenticate with Twitter API v2 using Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Define search parameters tailored to Indian companies
search_query = (
    "(Reliance OR TCS OR HDFC OR ICICI OR SBI OR Infosys OR ITC OR "
    "Unilever OR L&T OR HCL OR Bajaj OR NTPC OR Axis Bank OR "
    "Maruti OR Kotak OR Titan OR Tata Motors OR Zomato OR "
    "Adani OR Siemens OR #NIFTY50 OR #Sensex OR #BSE OR "
    "#NSE OR bullish OR bearish OR market rally OR earnings)"
)
tweet_limit = 100  # Max results per request is 100 for API v2

# Fetch tweets
tweets = client.search_recent_tweets(
    query=search_query,
    max_results=tweet_limit,
    tweet_fields=["created_at", "public_metrics", "text", "author_id"]
)

# Process tweets
data = []
if tweets.data:
    for tweet in tweets.data:
        data.append({
            "tweet_id": tweet.id,
            "author_id": tweet.author_id,
            "text": tweet.text,
            "created_at": tweet.created_at,
            "retweets": tweet.public_metrics["retweet_count"],
            "likes": tweet.public_metrics["like_count"]
        })

# Save data to a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv("indian_stock_tweets.csv", index=False)
print("Tweets saved to indian_stock_tweets.csv!")
