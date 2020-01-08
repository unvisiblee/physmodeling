import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.random import random as rand

num_steps = 100                                 # Set the number of steps for walk

bound = 20                                      # Set the size of figure 20x20
fig = plt.figure()
ax = plt.axes(xlim = (-bound, bound), ylim = (-bound, bound))

my_line = ax.plot([], [], lw = 2)[0]            # Line that will represent a path
my_point = ax.plot([], [], 'ro', ms = 9)[0]     # Dot that will represent a walker

x_steps = 2 * (rand(num_steps) < 0.5 ) - 1      # Generating arrays of 1 and -1
y_steps = 2 * (rand(num_steps) < 0.5 ) - 1

x_coords = x_steps.cumsum()
y_coords = y_steps.cumsum()

def get_step(n, x, y, this_line, this_point):   # n - frame number, x,y - coords
    this_line.set_data(x[:n + 1], y[:n + 1])    # this_line, this_point - 
    this_point.set_data(x[n], y[n])             # objects of line and point
    
my_movie = animation.FuncAnimation(fig, get_step, frames = num_steps, fargs = (x_coords, \
                                                   y_coords, my_line, my_point ))

# FFMPEG required !!!
my_movie.save('random_walk.mp4', fps = 10)