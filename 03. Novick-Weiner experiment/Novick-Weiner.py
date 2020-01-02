import numpy as np
import matplotlib.pyplot as plt

novick_data_set = np.loadtxt('g149novickA.csv', delimiter = ',') # Loading the data from a file
time_exp = novick_data_set[:, 0]                                 # Extracting time from the data
results_exp = novick_data_set[:, 1]                              # Extracting the values

tau = 3.5                                                        # Parameter that fits to our results

t = np.linspace(0, 6.7, 61)                                      
V = 1 - np.exp(-t/tau)                                           # V = 1 - e^(-t/tau) 

plt.figure()                                                     # Creating an empty figure 

plt.plot(t, V)                                                   # Drawing the model's plot 
plt.plot(time_exp, results_exp, 'or')                            # Drawing plot based on
                                                                 # the experiment
ax = plt.gca()
ax.set_xlabel("Time [hours]", size = 12)
ax.set_ylabel("Max. beta-galactosidase activity", size = 12)
ax.set_title("Novick-Weiner model", weight = 'bold')
ax.legend( ("Model prediction", "Experimental results") )        # Extra info to the plot