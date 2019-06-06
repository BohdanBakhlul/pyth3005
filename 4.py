import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data = np.load('dataBar3D.npy')
arr = np.arange(10)

arr1 = np.hstack([np.arange(10), np.arange(10), np.arange(10)])
arr2 = np.hstack([np.full(10, 1), np.full(10, 2), np.full(10, 3)])

col = np.hstack([np.full(10, 'g'), np.full(10, 'r'), np.full(10, 'b')])

fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')

ax1.bar(arr1, np.hstack(data), zs=arr2, zdir='y', color=col)

plt.show()
