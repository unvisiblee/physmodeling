import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit

novick_data_set = np.loadtxt('g149novickB.csv', delimiter = ',') # Loading the data from a file
time_exp = (np.array(novick_data_set[:, 0]))                     # Extracting time from the data 
time_exp = time_exp[time_exp < 10]                               # Choosing the times under 10 hours
results_exp = np.array(novick_data_set[:, 0])                    # Extracting the data
results_exp = results_exp[:time_exp.size]                        # Chosing the data corresponding to
                                                                 # the time

A = 6                                     # Parameters fitting to our results
tau = 3.5

time = np.linspace(0, 10, 61)             # Creating the times for the model

W = A * (np.exp(-time/tau) -1 + time/tau) # W(t) = A(e^(-t/tau) - 1 + t/tau)

plt.figure()                              # Creating an empty figure 

plt.plot(time, W)                         # Plot of model prediction
plt.plot(time_exp, results_exp, 'xr')     # Plot based on experimental data 

ax = plt.gca()
ax.set_xlabel("Time [hours]")
ax.set_ylabel("Max. beta-galactosidase activity")
ax.set_title("Novick-Weiner model", weight = 'bold')
ax.legend( ('Model prediction', 'Experimental results') )