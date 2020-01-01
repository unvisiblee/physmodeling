import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()                   # Create a figure
ax = Axes3D(fig)                     # 3D plotter for the figure
t = np.linspace(0, 50 * np.pi, 500)
ax.plot(np.cos(t), np.sin(t), t)     # Drawing a 3D Plot of Helix