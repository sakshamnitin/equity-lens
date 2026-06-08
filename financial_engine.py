"""
financial_engine.py
Pulls and normalises key financial metrics from yfinance.
Mirrors the ratio logic used in the McLaren DCF project.
"""

import math


def fmt_pct(val):
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return "N/A"
    return f"{val * 100:.1f}%"


def fmt_x(val):
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return "N/A"
    return f"{val:.1f}x"


def fmt_num(val):
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return "N/A"
    return f"{val:.2f}"


def fmt_large(val):
    """Format large numbers in B/M for readability."""
    if val is None:
        return "N/A"
    try:
        val = float(val)
    except (TypeError, ValueError):
        return "N/A"
    if abs(val) >= 1e9:
        return f"{val/1e9:.2f}B"
    if abs(val) >= 1e6:
        return f"{val/1e6:.2f}M"
    return f"{val:.0f}"


def compute_financials(stock, info: dict, hist) -> dict:
    """
    Returns a flat dict of display-ready financial metrics.
    All values are strings suitable for display and for the Claude prompt.
    """

    def g(key, default=None):
        v = info.get(key, default)
        if v in (None, "N/A", "", "Infinity"):
            return None
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    # Price & market data
    current_price = g("currentPrice") or g("regularMarketPrice") or g("previousClose")

    # 52-week return
    try:
        if len(hist) > 0:
            start_price = hist["Close"].iloc[0]
            end_price   = hist["Close"].iloc[-1]
            ret_52w = (end_price - start_price) / start_price
        else:
            ret_52w = None
    except Exception:
        ret_52w = None

    return {
        "current_price":    fmt_num(current_price),
        "pe_ratio":         fmt_x(g("trailingPE")),
        "forward_pe":       fmt_x(g("forwardPE")),
        "peg_ratio":        fmt_x(g("pegRatio")),
        "ev_ebitda":        fmt_x(g("enterpriseToEbitda")),
        "price_book":       fmt_x(g("priceToBook")),
        "price_sales":      fmt_x(g("priceToSalesTrailing12Months")),
        "debt_equity":      fmt_num(g("debtToEquity")),
        "current_ratio":    fmt_num(g("currentRatio")),
        "roe":              fmt_pct(g("returnOnEquity")),
        "roa":              fmt_pct(g("returnOnAssets")),
        "gross_margin":     fmt_pct(g("grossMargins")),
        "operating_margin": fmt_pct(g("operatingMargins")),
        "profit_margin":    fmt_pct(g("profitMargins")),
        "revenue_growth":   fmt_pct(g("revenueGrowth")),
        "earnings_growth":  fmt_pct(g("earningsGrowth")),
        "free_cash_flow":   fmt_large(g("freeCashflow")),
        "dividend_yield":   fmt_pct(g("dividendYield")),
        "beta":             fmt_num(g("beta")),
        "week52_high":      fmt_num(g("fiftyTwoWeekHigh")),
        "week52_low":       fmt_num(g("fiftyTwoWeekLow")),
        "return_52w":       fmt_pct(ret_52w),
        "market_cap":       fmt_large(g("marketCap")),
        "enterprise_value": fmt_large(g("enterpriseValue")),
    }
