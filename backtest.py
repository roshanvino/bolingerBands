import pandas as pd

def backtest_strategy(data):
    data['Returns'] = data['Close'].pct_change()
    data['Strategy Returns'] = data['Signal'].shift(1) * data['Returns']
    data['Cumulative Returns'] = (data['Strategy Returns'] + 1).cumprod()
    return data

if __name__ == "__main__":
    data = pd.read_csv('../data/stock_data_with_signals.csv', index_col='Date', parse_dates=True)

    data = backtest_strategy(data)
    data.to_csv('../data/backtest_results.csv')
