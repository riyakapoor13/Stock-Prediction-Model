import praw
import pandas as pd

# Reddit API credentials
reddit = praw.Reddit(
    client_id="YJDqnmNyXd2OUtbIABoVTA",
    client_secret="tyLPqI_Pz9xmhMfT2kDbGG_P7aWssw",
    user_agent="IndianStockScraper by /u/Difficult-Age9720"
)

# Define the subreddit and keywords
subreddit_name = "IndianStockMarket"  # Target subreddit
keywords = [
    "Reliance", "TCS", "Infosys", "HDFC Bank", "ICICI Bank", "SBI",
    "Bajaj Finance", "Adani", "Wipro", "ITC", "L&T", "HCL", "Titan", "NTPC",
    "Sensex", "NIFTY50", "BSE", "NSE", "midcap stocks", "largecap stocks",
    "bullish", "bearish", "crash", "rally", "earnings", "dividends", "buybacks",
    "IPO", "stock split", "banking stocks", "auto sector", "oil stocks",
    "energy sector", "renewable energy", "EV stocks", "Maruti", "Tata Motors",
    "inflation", "interest rates", "rate hikes"
]

# Fetch posts
posts = []
for submission in reddit.subreddit(subreddit_name).search(" OR ".join(keywords), limit=500):  # Fetch up to 500 posts
    posts.append({
        "title": submission.title,
        "score": submission.score,
        "id": submission.id,
        "url": submission.url,
        "created": submission.created_utc,
        "num_comments": submission.num_comments,
        "body": submission.selftext,
    })

# Save to DataFrame
df = pd.DataFrame(posts)

# Save DataFrame to CSV
df.to_csv("reddit_posts_extended.csv", index=False)
print("Extensive Reddit data saved to reddit_posts_extended.csv!")
