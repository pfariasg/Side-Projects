import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")


inputs = {
    'ticker': ['^GSPC', 'XLK'], # yahoo finance tickers
    'name': ['S&P500', 'XLK'], # security name
}

inputs = pd.DataFrame.from_dict(inputs)

# get data, forward-fill
prices = yf.download(inputs['ticker'].to_list(), '2019-01-01')['Adj Close']
prices.fillna(method='ffill', inplace=True)

prices.columns = [inputs[inputs['ticker'] == ticker]['name'].values[0] for ticker in prices.columns]

# daily returns (non-log)
changes = prices.pct_change().dropna()

# OLS between market returns (x) and asset returns (y)
x = changes[inputs['name'][0]]
y = changes[inputs['name'][1]]

reg = sm.OLS(y, x).fit()

# beta from the regression coefficient
beta_reg = reg.params.values[-1]

# beta = cov(x, y) / variance(x)
beta_cov = np.cov(x, y)[0][1]/np.var(x)

# beta = corr(x, y) * stdev(y) / stdev(x)
beta_corr = np.corrcoef(x, y)[0][1]*np.std(y)/np.std(x)


fig = plt.figure()
ax = fig.add_subplot()
# ax2 = fig.add_subplot(2,1,2)

ax.scatter(x, y)

x_h = np.linspace(x.min()-0.9*abs(x.min()),x.max()+0.9*abs(x.max()),2)
y_h = x_h * beta_reg
ax.plot(x_h, y_h, c='orange')

x_h = np.linspace(x.min()-0.9*abs(x.min()),x.max()+0.9*abs(x.max()),2)
ax.plot(x_h, x_h, c='k', ls='dashed', lw=.5)

ax.axhline(0, c='k', lw=.5)
ax.axvline(0, c='k', lw=.5)

ax.set_xlim(min(x.min(), y.min()), max(x.max(),y.max()))
ax.set_ylim(min(x.min(), y.min()), max(x.max(),y.max()))

ax.set_yticklabels(['{:,.1%}'.format(x) for x in ax.get_yticks()])
ax.set_xticklabels(['{:,.1%}'.format(x) for x in ax.get_xticks()])

ax.set_title(f"{inputs['name'][1]}'s beta with {inputs['name'][0]}: {round(beta_reg,3)}", fontsize=24)
ax.set_xlabel(inputs['name'][0], fontsize=12)
ax.set_ylabel(inputs['name'][1], fontsize=12)
ax.grid(which='both')

plt.show()

print('\n')
print(reg.summary())
print('\n\n')
print(f'beta from OLS:         {round(beta_reg,3)}')
print(f'beta from covariance:  {round(beta_cov,3)}')
print(f'beta from correlation: {round(beta_corr,3)}')

