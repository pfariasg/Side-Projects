import math
import matplotlib.pyplot as plt
import numpy as np

import sys

S0 = 100

u = 0.05
vol = 0.5
delta_t = 1/360
shape = [100, 3000]

e = np.random.normal(0,1,shape)
random_walk = 1 + u * delta_t + vol*e*np.sqrt(delta_t)

random_walk[0] += S0-1
random_walk = np.cumprod(random_walk, axis=0)


f, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[4, 1])
ax1.plot(random_walk)

ax2.hist(random_walk[-1], bins=50, orientation='horizontal')

print(np.mean(random_walk[-1])/(1+u*100/360)) #
print((np.std(random_walk[-1]/random_walk[0]-1))*np.sqrt(360/100))



ax1.set_xlim(left=0, right=len(random_walk))
ax1.set_ylim(bottom=min(np.min(random_walk)*1.3, np.min(random_walk)/1.3), top=np.max(random_walk)*1.3)
ax2.set_ylim(bottom=min(np.min(random_walk)*1.3, np.min(random_walk)/1.3), top=np.max(random_walk))
plt.show()

