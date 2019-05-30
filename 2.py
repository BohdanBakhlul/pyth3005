import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import stats

ex = np.linspace(-5, 5, 300)
data = np.load('rozklady.npz')
arr = []
arr.append(data['arr_0'])
arr.append(data['arr_1'])
arr.append(data['arr_2'])




a = stats.gaussian_kde(arr[0][0])
b = stats.gaussian_kde(arr[0][1])
#a = stats.gaussian_kde(arr[1][0])
#b = stats.gaussian_kde(arr[1][1])
#a = stats.gaussian_kde(arr[2][0])
#b = stats.gaussian_kde(arr[2][1])
plt.plot(a(ex))
plt.plot(b(ex))
plt.show()
