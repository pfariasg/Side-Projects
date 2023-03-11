import math
import numpy as np
import pandas as pd
import yfinance as yf

inputs = {
    'ticker': ['^GSPC', 'TSLA','^BVSP'], # yahoo finance tickers
    'name': ['S&P500', 'TESLA', 'IBOV'], # security name
    'weight': [0.25, 0.25, 0.50]          # weight on portfolio
}

inputs = pd.DataFrame.from_dict(inputs)

# get data, forward-fill
prices = yf.download(inputs['ticker'].to_list(), '2019-01-01')['Adj Close']
prices.fillna(method='ffill', inplace=True)

# get weight matrix and replace tickers by the security name (be mindful that yfinance reorders the given tickers)
weights = np.asmatrix([inputs[inputs['ticker'] == ticker]['weight'].values[0] for ticker in prices.columns]).T
prices.columns = [inputs[inputs['ticker'] == ticker]['name'].values[0] for ticker in prices.columns]

# daily returns (non-log)
changes = prices.pct_change().dropna()

print(changes.cov())

# covariance matrix
cov_mx = changes.cov().to_numpy()

# use matrix multiplication to get the portfolio standard deviation
p_variance = weights.T * cov_mx * weights
p_std = math.sqrt(p_variance)

print(f'Matrix multiplication method: portfolio stdev == {round(p_std, 6)}')

# another way of calculating portf. stdev: get standard deviation of the returns of the portfolio

changes['portfolio'] = changes.to_numpy() * weights

p_std = np.std(changes['portfolio'])

print(f'Weighted returns method:      portfolio stdev == {round(p_std, 6)}')