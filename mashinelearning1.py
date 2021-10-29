import numpy as np
from matplotlib import pyplot as plt
a = np.random.randint(1, 7, 100)
plt.hist(a, bins=6, edgecolor= 'red',alpha=1)
plt.show()