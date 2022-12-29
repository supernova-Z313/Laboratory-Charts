import matplotlib.pyplot as plt
import numpy as np

""" simple line with dot """
xpoints = np.array([0, 6, 10])
ypoints = np.array([0, 250, 130])
plt.plot(xpoints, ypoints, 'o') # add dots
plt.plot(xpoints, ypoints) # add lines0
plt.grid()
plt.show()
