# Bollinger Bands Mean Reversion Strategy

This project implements a Bollinger Bands mean reversion trading strategy. It includes fetching historical stock data, calculating Bollinger Bands, generating buy/sell signals based on the strategy, backtesting, and visualizing the results.

## Installation

1. Clone the GitHub repository to your local machine:
2. Install the required Python packages using `pip install -r requirements.txt`


## Usage

1. **Fetch Data**:
- Run `fetch_data.py` to fetch historical stock data and save it to `data/stock_data.csv`.

2. **Calculate Bollinger Bands**:
- Run `bollinger_bands_strategy.py` to calculate Bollinger Bands and generate buy/sell signals.

3. **Backtest**:
- Run `backtest.py` to backtest the trading strategy and calculate returns.

4. **Visualize Results**:
- Run `visualization.py` to visualize backtest results, including buy/sell signals.

## Results

- The backtest results are saved as `results/backtest_results.png`.
- Analyze the results to evaluate the performance of the trading strategy.

## Notes

- Adjust parameters such as ticker symbols, date ranges, and strategy parameters based on your requirements.
- Ensure file paths and dependencies are configured correctly for your environment.
- Feel free to experiment with different strategies or enhancements to improve performance.
- If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.
