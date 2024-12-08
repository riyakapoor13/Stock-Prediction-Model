import praw

# Updated Reddit API credentials
reddit = praw.Reddit(
    client_id="YJDqnmNyXd2OUtbIABoVTA",  # Updated Client ID
    client_secret="tyLPqI_Pz9xmhMfT2kDbGG_P7aWssw",  # Updated Client Secret
    user_agent="IndianStockScraper by /u/Difficult-Age9720"  # Your Reddit username
)

# Test Reddit connection
try:
    print("Authenticated user:", reddit.user.me())
except Exception as e:
    print(f"Authentication failed: {e}")
