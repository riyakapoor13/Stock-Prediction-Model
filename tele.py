from telethon.sync import TelegramClient
import pandas as pd

# Replace with your API credentials
api_id = 23487884  # Your API ID
api_hash = "d36a5de11582bc3df129330125804f9c"  # Your API Hash
group_username = "stockmarketindia"  # Replace with the channel/group username

# Define keywords to filter messages
keywords = [
    "Reliance", "TCS", "Infosys", "HDFC", "ICICI", "SBI", "Adani", "Sensex",
    "NIFTY50", "BSE", "bullish", "bearish", "inflation", "IPO", "dividends"
]

# Connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Fetch and filter messages
messages = []
for message in client.iter_messages(group_username, limit=500):  # Adjust limit as needed
    if message.text and any(keyword in message.text for keyword in keywords):
        messages.append({
            "date": message.date,
            "sender_id": message.sender_id,
            "text": message.text
        })

# Save messages to a DataFrame
df = pd.DataFrame(messages)

# Save DataFrame to CSV
df.to_csv("telegram_filtered_messages.csv", index=False)
print("Filtered Telegram data saved to telegram_filtered_messages.csv!")
