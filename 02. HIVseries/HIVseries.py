import numpy as np
import matplotlib.pyplot as plt

"""
 We have the 2 plots: 1 we drawing from a dataset that we got 
 from the experiment, second we draw using the model formula
 with adjusted parameters (A, B, alpha, beta).

 The aim of the script is to compare two plots and see the 
 result
"""


hiv_data_set = np.loadtxt('HIVseries.csv', delimiter = ',') # Loading the data from a file

time = hiv_data_set[:, 0]                                   # Extracting the time from the data
viral_load_exp = hiv_data_set[:, 1]                         # Extracting the load from the data

A = 73000                                                   # Values that will fit our model
B = 72000                                                   # to the experimental results
alpha = 0.88
beta = 0.25
                                                            # V(t) = A * exp(-at) + B * exp(-bt)   
viral_load = A * np.exp(- alpha * time) + B * np.exp(-beta * time) 

plt.figure()                                                # Creating a figure for the plot 
plt.plot(time, viral_load_exp, 'xr')                        # Drawing a plot based on the data
plt.plot(time, viral_load, 'b')                             # Drawing a plot based on the model

ax = plt.gca()

ax.set_ylabel("Bacteries concentration", size = 12)         # Add extra info to the legend and ases
ax.set_xlabel("Time, [days]", size = 12)
ax.set_title("HIV infection course time", weight = 'bold', size = 18)
ax.legend( ('Experimental results', 'Model expectation') )