import numpy as np
import matplotlib.pyplot as plt

coords = np.linspace(-2, 2, 101)
X,Y = np.meshgrid(coords[::5], coords[::5])      # Setting up the grid for a vector field
R = np.sqrt(X ** 2 + Y ** 2)                     # R(x,y) = x^2 + y^2
Z = np.exp(-R ** 2)                              # Z(R) = e^(-R^2)
x, y = np.meshgrid(coords, coords)               # Grid for the future isoline (contour line)
r = np.sqrt(x ** 2 + y ** 2)
z = np.exp(-r ** 2)                              # The same functions for the plot   

ds = coords[6] - coords[0]                       # Spacing between values
dX, dY = np.gradient(Z, ds)                      # Calculating the gradient

plt.contourf(x, y, z, 25)                        # Drawing the isoline               
plt.set_cmap('coolwarm')
plt.quiver(X, Y, dX.transpose(), dY.transpose(), scale = 25, color = 'k') # Drawing the vector field