import yfinance as yf
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

window = 44

ticker_dict = {
    '^GSPC': 'S&P500', 
    '^BVSP': 'IBOV'

}

prices = yf.download(list(ticker_dict.keys()), '2019-01-01')['Adj Close']

tickers = [ticker_dict[x] for x in prices.columns]
prices.columns = tickers
tickers = list(ticker_dict.values())


prices = prices.fillna(method='ffill')
df = prices.pct_change().dropna()




# print(df.head())
corrs = df.rolling(window).corr()
corrs = corrs.swaplevel()
corrs = corrs.loc[tickers[0], tickers[1]]
corrs.dropna(inplace=True)

print(corrs.tail())

fig, ax1 = plt.subplots()
ax1.set_ylabel('correlation', fontsize=12)
ax1.set_ylim(-1,1)
ax1.plot(corrs)

ax2 = ax1.twinx()
cum_return = prices[tickers[0]].pct_change(periods=window, fill_method='ffill')
cum_return.dropna(inplace=True)
ax2.plot(cum_return, color='tab:orange')
ax2.set_ylim(-.5,.5)
ax2.set_yticks(np.arange(-.5,.5,.125))
ax2.set_ylabel('accumulated return', fontsize=12)

fig.legend(['correlation', f'{tickers[0]} accumulated return'], loc=8, fontsize=12)
ax1.axhline(0,c='k')
ax1.grid(which='both')
fig.suptitle(f'{tickers[0]} and {tickers[1]} correlation + {tickers[0]} return', fontsize=24)
ax1.set_title(f'{window} days window', fontsize=20)


plt.show()


# regression
# y = df[tickers[0]]
# x = df[tickers[1]]
# x = sm.add_constant(x)

# reg = sm.OLS(y, x)
# res = reg.fit()

# coefs = res.params

# print(res.summary())
# print(df.cov())

# plt.scatter(df[tickers[1]], df[tickers[0]])
# x = np.linspace(df[tickers[1]].min()*1.1,df[tickers[1]].max()*1.1,1000)
# y = coefs['const'] + x * coefs[tickers[1]]
# plt.plot(x, y, c='orange')
# plt.show()