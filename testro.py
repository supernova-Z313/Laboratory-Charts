# import matplotlib.pyplot as plt
# import numpy as np

# """ simple line with dot """
# xpoints = np.array([0, 6, 10])
# ypoints = np.array([0, 250, 130])
# plt.plot(xpoints, ypoints, 'o') # add dots
# plt.plot(xpoints, ypoints) # add lines0
# plt.grid()
# plt.show()
# =======================================================

""" plot sin shape """
import numpy as np
import matplotlib.pyplot as plt

# define a list of markevery cases to plot
cases = [
    None,
    8,
    (30, 8),
    [16, 24, 32],
    [0, -1],
    slice(100, 200, 3),
    0.1,
    0.4,
    (0.2, 0.4)
]

# data points
delta = 0.11
x = np.linspace(0, 10 - 2 * delta, 200) + delta
y = np.sin(x) + 1.0 + delta
# plt.plot(x, y)
# plt.show()

fig, axs = plt.subplots(3, 3, figsize=(10, 6), constrained_layout=True)
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)

plt.show()

# ====================================================================