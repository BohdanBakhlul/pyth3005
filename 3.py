import matplotlib.pyplot as plt
import numpy as np

data = np.load('dataBar3D.npy')
arr = np.arange(10)

print(data)

plt.bar(arr, data[0], bottom=data[1]+data[2])
plt.bar(arr, data[1], bottom=data[2])
plt.bar(arr, data[2])

plt.show()
