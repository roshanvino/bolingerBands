from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()


def fetch_stock_data(tickers, start_date, end_date):
    data = pdr.get_data_yahoo(tickers, start=start_date, end=end_date)
    return data


if __name__ == "__main__":
    tickers = ['AAPL']  # Example tickers i.e. AAPL
    start_date = '2020-01-01'
    end_date = '2024-01-01'

    stock_data = fetch_stock_data(tickers, start_date, end_date)
    stock_data.to_csv('data/stock_data.csv')
