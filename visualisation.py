import matplotlib.pyplot as plt
import pandas as pd


def visualise_results(data):
    plt.figure(figsize=(10, 6))
    data['Close'].plot(label='Close Price')
    plt.scatter(data[data['Signal'] == 1].index, data['Close'][data['Signal'] == 1], marker='^', color='g',
                label='Buy Signal')
    plt.scatter(data[data['Signal'] == -1].index, data['Close'][data['Signal'] == -1], marker='v', color='r',
                label='Sell Signal')
    plt.title('Bollinger Bands Mean Reversion Strategy')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.savefig('../results/backtest_results.png')


if __name__ == "__main__":
    data = pd.read_csv('../data/backtest_results.csv', index_col='Date', parse_dates=True)

    visualise_results(data)
