import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")

inputs = {
    'ticker': ['^GSPC', 'XLK', 'XLI', 'XLU', 'XTN', 'XLE'], # yahoo finance tickers
    'name':  ['S&P500', 'XLK', 'XLI', 'XLU', 'XTN', 'XLE'], # security name
}

inputs = pd.DataFrame.from_dict(inputs)

# get data, forward-fill
prices = yf.download(inputs['ticker'].to_list(), '2019-01-01')['Adj Close']
prices.fillna(method='ffill', inplace=True)

prices.columns = [inputs[inputs['ticker'] == ticker]['name'].values[0] for ticker in prices.columns]

# daily returns (non-log)
changes = prices.pct_change().dropna()

# covariance matrix
cov = np.asmatrix(changes.cov())

# matrix with inverse of variance on the diagonal and 0 otherwise
inv_var_matrix = 1/np.diag(np.diag(cov))
inv_var_matrix[inv_var_matrix == np.inf] = 0

# beta matrix
beta_matrix = cov * inv_var_matrix

beta_matrix = pd.DataFrame(beta_matrix, columns=changes.columns, index=changes.columns)

print(beta_matrix)
