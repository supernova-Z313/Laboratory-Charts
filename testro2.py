import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6 , 7, 8]
y = [10.2, 11.5, 12, 13, 13.9, 14.5, 15, 16.3]


# plot with various axes scales
fig, axs = plt.subplots(1, 2, figsize=(7, 5))

# linear
ax = axs[0]
ax.plot(x, y, '-', lw=2)
ax.plot(x, y)
ax.set_yscale('linear')
ax.set_title('linear')
ax.grid(True)

plt.show()
