import numpy as np
import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5, 6 , 7, 8]
# y = [10.2, 11.5, 12, 13, 13.9, 14.5, 15, 16.3]
#
#
# # plot with various axes scales
# fig, axs = plt.subplots(1, 2, figsize=(7, 5))
#
# # linear
# ax = axs[0]
# ax.plot(x, y, '-', lw=2)
# ax.plot(x, y)
# ax.set_yscale('linear')
# ax.set_title('linear')
# ax.grid(True)
#
# plt.show()
# np.pi*2
fig, axs = plt.subplots(1, 1)
x = np.linspace(0, 330, 500)
y = np.sin(x/52.5) + 0.74
plt.plot(x, y, "o", ls="-", ms=4, markevery=[0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 310, 329])
# axs.plot(x, y)
axs.grid()
axs.set_title("Experiment(8): Graph-2 Voltage changes at different angles.")
axs.set_xlabel("")
axs.set_ylabel("V(v)")
plt.show()
# ==========================================
""" for morabaei shape get one state top one but tol har khat , baze v generate them"""
"""
https://matplotlib.org/stable/gallery/scales/scales.html#sphx-glr-gallery-scales-scales-py
https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#sphx-glr-gallery-lines-bars-and-markers-markevery-demo-py
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html
"""

