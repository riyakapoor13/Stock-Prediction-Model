import tweepy

# Replace with your keys and tokens
api_key = "Llm4AmbvtCe47QfGC8muYjhRX"
api_key_secret = "Y352EJOiiZR3uZoFIRfN8VneMSiXonirKnbrxhCGZWJIhWptd2"
access_token = "1865357447105519616-IwEDixILE2VaVS5avwL2WxDKOWDdc6"
access_token_secret = "EVHLbVRz9EFiaCzlfrocbD1A33RvC7ZPxBDe1xcYdP7oV"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Test connection
try:
    api.verify_credentials()
    print("Authentication successful!")
except Exception as e:
    print("Error during authentication:", e)
