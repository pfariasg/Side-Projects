import datetime
from math import exp, cos, log, sqrt, pi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Calculates the approximated area beween a function and the x axis (y=0) given two points on the x axis using an increasing number of random samples.
# Then plots the resulting area and the time taken to calculate it. If all is right, the graph will show a reducing error in the calculated areas (smaller standard deviation)
# and convergence into what would be the true analytical result of the integral of the funcion f(x).

low_x  =  0 # point at x where the area starts
high_x = 10 # point at x where the area ends

num_simulations = 100 # num of iterations of increased 1000 (x, y) samples. For example, if == 2, calculates the area using 1000 samples and calculates again using 2000 samples. 

# define function
def f(x):
    f = -2 * exp(x) * (cos(x)+log(x + pow(2, sqrt(1/(x+1) + x)))) / (sqrt(x)+pow(x, 2)-pow(pi,x))

    return f

##################################################################################################

start = datetime.datetime.now()

#  low y is always 0
max_y = max(f(np.linspace(low_x, high_x, 10000))) # max y is max f

f = np.vectorize(f) # make f ready for numpy arrays

results = []
run = datetime.datetime.now() # 'run' calculates how long a single simulation runs
for i in range(num_simulations): # run 100 simulations

    tries = 1000 * (i+1) # each with 1000 more dots

    sampl = np.random.uniform(low=(low_x, low_x), high=(high_x, max_y), size=(tries,2)) # uniformly distributed array. each row is a sample (dot), col 0 is x, col 1 is y

    indicator = sampl[:, 1] < f(sampl[:, 0]) # how many sampled y's (col 1) are below (<) the function (f(col 0))
    ratio = sum(indicator)/len(indicator)    # % of dots below the function
    
    time = datetime.datetime.now() - run
    run += time
    
    results.append([tries, ratio, time]) # save data about simulation

    if i % 10 == 0: # count each 10 simulations
        print(i)


df = pd.DataFrame(results, columns=['tries', 'area', 'time'])
df['area'] *= (high_x - low_x)*(max_y - low_x) # multiply % of dots below f(x) by known area

print(df.tail())
df.to_clipboard()

print(datetime.datetime.now() - start)

# plot # of samples -> time | # of samples -> approx. area

fig, ax1 = plt.subplots()
ax1.set_xlabel('tries')
ax1.set_ylabel('area')
ax1.plot(df['tries'],df['area'])

ax2 = ax1.twinx()
ax2.set_xlabel('tries')
ax2.set_ylabel('time')
ax2.plot(df['tries'],df['time'], c='tab:orange')

fig.legend(['area', 'time'], loc=8)

fig.tight_layout()
plt.show()