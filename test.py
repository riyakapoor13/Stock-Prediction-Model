from telethon.sync import TelegramClient
import pandas as pd

# API credentials (Replace these with your actual credentials)
api_id = 23487884  # Your API ID
api_hash = "d36a5de11582bc3df129330125804f9c"  # Your API Hash
group_username = "https://t.me/Indian_Share_Stocks_Market_Tip"  # Telegram group invite link

# Connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Initialize list to store messages
messages = []

# Fetch messages
try:
    for message in client.iter_messages(group_username, limit=2000):  # Adjust limit as needed
        if message.text:  # Only include messages with text
            messages.append({
                "date": message.date,
                "sender_id": message.sender_id,
                "text": message.text
            })
    print("Messages fetched successfully!")
except Exception as e:
    print(f"Error: {e}")

# Save messages to a DataFrame
if messages:
    df = pd.DataFrame(messages)
    df.to_csv("telegram_group_messages.csv", index=False)
    print("Messages saved to telegram_group_messages.csv!")
else:
    print("No messages were fetched.")
