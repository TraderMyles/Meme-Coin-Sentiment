# Meme Coin Sentiment Tracker 🐶📈

## 🚀 Overview
A real-time sentiment analysis for trending meme coins like DOGE, SHIB, and PEPE by scraping Reddit, analyzing the attitudes of posts, and correlating it with price data. Built with FastAPI, PostgreSQL, and deployed via AWS with Terraform.

---

## 🎯 Goals
- Collect social media posts about meme coins (Reddit)
- Perform sentiment analysis using NLP tools (e.g., VADER)
- Collect price data from CoinGecko API
- Store all raw and processed data in PostgreSQL
- Expose FastAPI endpoints for querying sentiment and price trends
- Deploy on AWS with Terraform and Docker

---

## 🧱 Tech Stack
- **Backend**: Python, FastAPI
- **NLP**: NLTK, VADER Sentiment
- **Scraping/APIs**: PRAW, CoinGecko
- **Database**: PostgreSQL + SQLAlchemy
- **Infrastructure**: Docker, Terraform, AWS EC2 + RDS

---

## 🗂 Project Structure
```
/data                # Static files (e.g., meme_coins.json)
/src                 # Core application code
  /api               # FastAPI routes
  /db                # DB models and utils
  /services          # Scrapers, sentiment analyzers
/tests               # Unit tests
README.md
requirements.txt
```

---

## 🔌 API Endpoints (Planned)
- `GET /sentiment/{{coin}}` – Sentiment scores over time
- `GET /price-sentiment/{{coin}}` – Correlation chart
- `GET /top-posts/{{coin}}?sentiment=positive` – Most hyped posts

---

## 🔄 Data Flow
1. Load coin metadata from `meme_coins.json`
2. Scrape posts from Reddit and Twitter
3. Analyze sentiment using NLP
4. Pull real-time prices from CoinGecko
5. Store everything in PostgreSQL
6. Expose data via FastAPI routes

---

## 📦 Installation & Running Locally
```bash
git clone https://github.com/yourname/meme-coin-sentiment-tracker.git
cd meme-coin-sentiment-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file and add your API keys.

---

## 🗺 Roadmap
- [x] Create project scaffold and folder structure
- [x] Generate `meme_coins.json`
- [ ] Scrape Reddit posts
- [ ] Get real-time prices
- [ ] Perform sentiment analysis
- [ ] Build FastAPI endpoints
- [ ] Deploy to AWS using Terraform

---

## 🤝 Contributing
This is a solo learning project for now, but pull requests and feedback are welcome.

---

## 📄 License
MIT License
