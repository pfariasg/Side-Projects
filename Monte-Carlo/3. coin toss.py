import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# simulates "num_path" distinct games in which a coin is tossed "legth" times. 
# The game yields +1 for each head and -1 for each tail with equal probability. 

# Firts calculates and displays a single path, then calculates and displays "num_paths" paths

length = 50
num_paths = 1000
# 0 == T, 1 == H

#################################################################

# calculating a single path
𝜖 = np.random.choice([0, 1], length)

def f(x):
    x = np.where(x == 0, -1, 1) # f(0) == -1, f(1) == 1

    return x
f = np.vectorize(f)

test = np.cumsum(f(𝜖)) 

plt.plot(test)
plt.show(block=False)
sleep(5)
plt.close()

# calculating multiple paths
𝜖 = np.random.choice([0, 1], (length, num_paths))

def f(x):
    x = np.where(x == 0, -1, 1) # f(0) == -1, f(1) == 1

    return x
f = np.vectorize(f)

test = np.cumsum(f(𝜖), axis=0) 

plt.plot(test)
plt.show(block=False)
sleep(5)
plt.close()

print(f'{np.average(test[-1,:])}')