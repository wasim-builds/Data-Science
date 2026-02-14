# Finance Dashboard Project

Build a stock market analysis tool using Python.

## 📂 Project Structure

### 1. [Stock Data Extraction](01_stock_data_extraction.ipynb)
- Uses `yfinance` API to download real-time market data.
- Fetches Adjusted Close prices for tech giants (AAPL, MSFT, GOOGL, AMZN).
- Calculates Daily Returns.

### 2. [Portfolio Analysis](02_portfolio_analysis.ipynb)
- **Correlation Matrix:** Do stocks move together?
- **Risk vs Return:** Scatter plot of Volatility vs Annual Return.
- **Cumulative Returns:** Growth of a $1 investment over time.

## 🚀 How to Run
1. Run `pip install yfinance`
2. Run `01_stock_data_extraction.ipynb` to download data.
3. Run `02_portfolio_analysis.ipynb` to analyze risk and return.

## 📊 Key Skills
- API Integration (Yahoo Finance)
- Financial Metrics (CAGR, Volatility, Sharpe Ratio)
- Time Series Visualization

## ⚠️ Note
This is for educational purposes only. Do not use for actual trading!
