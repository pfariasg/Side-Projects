import datetime
from math import exp, cos, log, sqrt, pi
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

# Calculates the approximate area below or above a user defined function (f(x)). Takes two points in the x axis (low_x and high_x) 
# and two points in the y axis (low_y and high_y), 

low_x  =   0  
high_x =  10 # point at x where the area ends

low_y  =   0 # point at y where the known area starts. if low_y < high_y, calculates area between low_y and the function. if low_y > high_y, calculates area between high_y and the function
high_y =  10 # point at y where the known area ends

tries  = 1e5 # how many (x,y) samples will be used to calculate de area

# function to be integrated
def f(x):
    f = -2 * exp(x) * (cos(x)+log(x + pow(2, sqrt(1/(x+1) + x)))) / (sqrt(x)+pow(x, 2)-pow(pi,x))
    # f = 2
    return f

##################################################################################################

start = datetime.datetime.now()

# grey area at which each dot will be placed
_, ax = plt.subplots(1)
ax.fill_between([low_x,high_x], [high_y, high_y], [low_y, low_y],color='#d5d0cd')


# blue area corresponds to the area to be calculated
x_1 = np.linspace(low_x,high_x, 10000)
y_1 = [f(x) for x in x_1]
l_1 = [low_y for _ in x_1]
ax.fill_between(x_1, y_1, l_1,alpha=0.8)


# plot x -> f(x)
x = np.linspace(min(0, low_x),high_x*1.1,10000)
y = [f(x) for x in x]

ax.plot(x, y)
ax.set_xlim(left=min(x), right=max(x))

plt.show(block=False)
sleep(5)

sampl_x = np.random.uniform(low=low_x, high=high_x, size=(int(tries),))
sampl_y = np.random.uniform(low=low_y, high=high_y, size=(int(tries),))
ax.scatter(sampl_x,sampl_y, alpha=0.7)

plt.show(block=False)
sleep(5)
plt.close()

# calculates how many dots are inside the blue area
indicator = []
for i in range(int(tries)):
    if (abs(sampl_y[i] - low_y) < abs(f(sampl_x[i])- low_y)) and ((sampl_y[i] - low_y) < 0) == ((f(sampl_x[i])- low_y) < 0):
        if (sampl_y[i] - low_y) > 0:
            indicator.append(1)
        else:
            indicator.append(-1)
    else:
        indicator.append(0)

# calculates % of dots inside the blue area and multiplies by grey (known) area
area = round(sum(indicator)/len(indicator), 5) * (high_x - low_x)*(high_y - low_y)

print(f'Estimated area: {round(area,4)}')

print(f'\nElapsed time: {datetime.datetime.now() - start}')