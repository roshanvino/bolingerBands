import pandas as pd


def calculate_bollinger_bands(data, window):
    data['Rolling Mean'] = data['Close'].rolling(window=window).mean()
    data['Upper Band'] = data['Rolling Mean'] + 2 * data['Close'].rolling(window=window).std()
    data['Lower Band'] = data['Rolling Mean'] - 2 * data['Close'].rolling(window=window).std()
    return data


def generate_signals(data):
    data['Signal'] = 0
    data.loc[data['Close'] < data['Lower Band'], 'Signal'] = 1  # Buy Signal
    data.loc[data['Close'] > data['Upper Band'], 'Signal'] = -1  # Sell Signal
    return data


if __name__ == "__main__":
    data = pd.read_csv('data/stock_data.csv', index_col='Date', parse_dates=True)
    window = 20  # Bollinger Bands window

    data = calculate_bollinger_bands(data, window)
    data = generate_signals(data)
    data.to_csv('data/stock_data_with_signals.csv')
