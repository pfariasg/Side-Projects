import math
import matplotlib.pyplot as plt
import numpy as np

import sys

delta_t = 1
shape = [100, 500]

e = np.random.normal(0,1,shape)
e *= np.sqrt(delta_t)

det = np.full(shape, -.25)

random_walk = np.cumsum(e+det, axis=0)

f, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[4, 1])
ax1.plot(random_walk)

ax2.hist(random_walk[-1], bins=50, orientation='horizontal')


print(np.mean(random_walk[-1]))
print(np.std(random_walk[-1]))



ax1.set_xlim(left=0, right=len(random_walk))
ax1.set_ylim(bottom=min(np.min(random_walk)*1.3, np.min(random_walk)/1.3), top=np.max(random_walk)*1.3)
ax2.set_ylim(bottom=min(np.min(random_walk)*1.3, np.min(random_walk)/1.3), top=np.max(random_walk))
plt.show()

