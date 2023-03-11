import math
import matplotlib.pyplot as plt
import numpy as np

# Simulates stock price movements using Hull's and Shreve's formulas for Monte Carlo simulations for financial assets. 

S0 = 100 # Stock price at t = 0
r_y = .1175  # yearly risk-free rate

t = 1   # time in years to be simulated 
n = 252*t # number of steps in the simulation
delta_t = t/n # how long each step takes

𝜎 = 0.35 # annualized vols

num_simulations = 500

#################################################################

# Hull cap. 4
np.random.seed(0)
r = pow(1+r_y, delta_t) - 1 # getting the risk-free rate for a single step from the yearly risk-free rate. See Hull's "Options, Futures and Other Derivatives" chapter 4.
𝜖 = np.random.normal(0,1,[n,num_simulations]) # standard normal random variable matrics (each step is a row, each simulation is a column)

returns = r + 𝜎*𝜖*math.sqrt(delta_t) # Formula presented in Hull's "Options, Futures and Other Derivatives" chapter 21 (dS = r S dt + 𝜎 S dz)
returns += 1
returns[0] *= S0

prices = np.cumprod(returns, axis=0)

returns_easy = prices[-1,:]/S0-1

returns = np.exp((r_y-(𝜎**2)/2)*t + 𝜎*𝜖[0,:]*math.sqrt(t))-1 

f, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[4, 1])
ax1.plot(prices)
# ax1.set_ylim(bottom=0, top=np.max(prices))
ax1.set_xlim(left=0, right=n)

ax2.hist(prices[-1,:], bins=50, orientation='horizontal')
# ax2.set_ylim(bottom=0, top=np.max(prices))
plt.show()

f, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[4, 1])
ax1.plot(np.log(prices))
# ax1.set_ylim(bottom=0, top=np.max(np.log(prices)))
ax1.set_xlim(left=0, right=n)

ax2.hist(np.log(prices)[-1,:], bins=50, orientation='horizontal')
# ax2.set_ylim(bottom=0, top=np.max(np.log(prices)))
plt.show()

_, bins, _ = plt.hist(returns, bins=50, alpha = 0.7, label='log returns')
plt.hist(returns_easy, bins=bins, alpha = 0.7, label='scalar returns')
plt.legend()
plt.show()

_, bins, _= plt.hist(np.log(returns+1), bins=50, alpha = 0.7, label='log returns')
plt.hist(np.log(returns_easy+1), bins=bins, alpha = 0.7, label='scalar returns')
plt.legend()
plt.show()
