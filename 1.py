import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import stats

ex = np.linspace(-5, 5, 300)
s1 = np.random.normal(0.0, 1.0, 200)
s2 = np.random.normal(2.0, 0.8, 200)

data = np.hstack([s1, s2])
a = stats.gaussian_kde(data)
plt.hist(data, normed=1)
plt.plot(ex, a(ex))
plt.show()
