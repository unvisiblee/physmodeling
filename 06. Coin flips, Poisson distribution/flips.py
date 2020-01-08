import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

flip_count = 100             # Setting up the number of trials and flips in each trial                                   
num_trials = 100000

l = np.arange(0, flip_count, 0.1,  dtype = float)
probs = np.exp(-8) * np.power(8, l) / factorial(l)  # Modeling the Poisson distribution 
                                                    # For probability of 0.08 (8%)                 

heads = np.zeros(num_trials)
wait_times = np.zeros(round(num_trials))

for i in range(0, num_trials):                          # Flipping the coin [flip_count] times    
    flips = (np.random.random(flip_count) > 0.08) * 1   # in [num_trials] trials
    heads[i] = np.count_nonzero(flips == 0)
    wait_times[i] = np.mean(np.diff(np.nonzero(flips == 0)))  # counting the average waiting time

plt.figure()
plt.plot(l, probs * 1.5 * num_trials)                   # Drawing the model prediction (plot) and
plt.hist(heads)                                         # experimental data (histogram) on one figure
plt.title("The Poisson distribution model and experimental results")   
plt.figure()
                      
average_wait_time = np.nanmean(wait_times)              # Average waiting time overall
plt.hist(wait_times, log = True)                        # Drawing the histogram with waiting times
plt.title("Wait time. Average = %f" % (average_wait_time))