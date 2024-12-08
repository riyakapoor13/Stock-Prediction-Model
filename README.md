# 🚀 **Stock Market Sentiment Analysis and Prediction**

📊 Predict stock market trends using **sentiment analysis** and **machine learning** on real-time data from **Twitter**, **Reddit**, and **Telegram**.

---

## **✨ Features**
- 🗂️ **Data Collection**: Scraped live stock-related discussions from social media platforms.
- 🧹 **Preprocessing**: Enhanced data with feature engineering for accurate analysis.
- 📈 **EDA**: Visualized stock trends, mentions, and sentiment distributions.
- 🤖 **ML Models**: Built and tested **LightGBM**, **XGBoost**, and regression models for sentiment-based predictions.

---

## **📂 Key Files**
| File                     | Purpose                                     |
|--------------------------|---------------------------------------------|
| `auth.py`                | 🛡️ Twitter API Authentication.             |
| `etweet.py`, `redde.py`, `tele.py` | 🔍 Scrape Twitter, Reddit, and Telegram. |
| `merge.py`               | 🧬 Combine all datasets into one.           |
| `feateng.py`             | 🛠️ Feature engineering on merged data.     |
| `visualisation.py`       | 📊 Create sentiment and trend visualizations. |
| `light.py`, `xgb.py`     | ⚡ Train ML models for predictions.         |

---

## **📄 Datasets**
| Dataset                          | Description                              |
|----------------------------------|------------------------------------------|
| `enhanced_twitter_data.csv`      | 🐦 Preprocessed Twitter data.            |
| `enhanced_reddit_data.csv`       | 🧵 Preprocessed Reddit data.             |
| `enhanced_telegram_data.csv`     | 📬 Preprocessed Telegram data.           |
| `featen_daily_data.csv`          | 🌞 Daily trends and features.            |
| `featen_hourly_data.csv`         | ⏰ Hourly trends and features.           |

---

## **📊 Outputs and Results**

### **🔍 Visual Insights**
- **📈 Top Stock Mentions**: Reliance, TCS, Infosys, HDFC, and more emerge as the most discussed stocks across social platforms.
- **📊 Sentiment Trends**: Positive sentiments dominate with bullish trends, but spikes in negative sentiments hint at market volatility.
- **🕒 Hourly and Daily Trends**: Observed trends reveal peak discussion times and critical sentiment shifts tied to market events.

---

## **🌟 Project Impact**
This project bridges the gap between **social media sentiments** and **stock market movements**, offering actionable insights and high-performing models. With **robust preprocessing**, **in-depth analysis**, and **cutting-edge machine learning techniques**, it sets a **benchmark** for predicting market trends from unstructured data. 

> **✨ Future Scope**: Incorporating live-streamed data and extending to global markets can elevate its potential as a comprehensive financial analytics tool.

🎉 **Join the journey of turning data into decisions and insights into innovation!**
