import matplotlib.pyplot as plt
import numpy as np

import sys

delta_t = 1

e = np.random.normal(0,1,[100, 2000])
e *= np.sqrt(delta_t)

random_walk = np.cumsum(e, axis=0)

# print(random_walk)
# sys.exit()

f, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[4, 1])
ax1.plot(random_walk)

ax2.hist(random_walk[-1], bins=50, orientation='horizontal')


print(np.mean(random_walk[-1]))
print(np.std(random_walk[-1]))



ax1.set_xlim(left=0, right=len(random_walk))
ax1.set_ylim(bottom=min(np.min(random_walk)*1.3, np.min(random_walk)/1.3), top=np.max(random_walk)*1.3)
ax2.set_ylim(bottom=min(np.min(random_walk)*1.3, np.min(random_walk)/1.3), top=np.max(random_walk))
plt.show()

