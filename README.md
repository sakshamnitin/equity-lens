# EquityLens – AI Equity Research Report Generator

Institutional-style, one-page equity research reports for any stock ticker.
Built with Streamlit · yfinance · Claude API · fpdf2.

---

## Features
- Live financial data via yfinance (US, NSE, BSE, global tickers)
- Valuation analysis powered by Claude (DCF logic, comps, narrative)
- Clean PDF download — valuation summary, key ratios, risk flags, verdict
- 100% Python — no frontend skills needed

---

## Local Setup

```bash
# 1. Clone / unzip the project
cd equity_research_app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
streamlit run app.py
```

Open http://localhost:8501, paste your Anthropic API key in the sidebar, enter a ticker.

---

## Deploy to Streamlit Cloud (Free)

1. Push this folder to a GitHub repo (public or private)
2. Go to https://share.streamlit.io → "New app"
3. Select your repo · branch · set `app.py` as the main file
4. Under **Advanced settings → Secrets**, add:
   ```toml
   # Optional: pre-fill the API key so users don't need to enter it
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
5. Click Deploy — live in ~2 minutes

**To use the secret in app.py**, replace the api_key input with:
```python
import os
api_key = st.secrets.get("ANTHROPIC_API_KEY") or st.sidebar.text_input("Anthropic API Key", type="password")
```

---

## Monetisation Ideas

| Model | How |
|---|---|
| Freemium | 3 free reports/day, paid plan for unlimited |
| Pay-per-report | Stripe payment link before PDF download |
| Subscription | Gumroad or Lemon Squeezy for ₹499/mo |
| White-label | Sell to small wealth managers as a branded tool |

---

## Supported Tickers

| Market | Format | Example |
|---|---|---|
| US (NYSE/NASDAQ) | TICKER | AAPL, MSFT, TSLA |
| NSE India | TICKER.NS | RELIANCE.NS, TCS.NS |
| BSE India | TICKER.BO | RELIANCE.BO |
| London | TICKER.L | HSBA.L |
| Frankfurt | TICKER.DE | BMW.DE |

---

## Tech Stack

- **Streamlit** – UI framework
- **yfinance** – Free financial data (Yahoo Finance)
- **Anthropic Claude** – Valuation narrative + verdict
- **fpdf2** – PDF generation

---

*Built by Saksham Minde · Not investment advice*
