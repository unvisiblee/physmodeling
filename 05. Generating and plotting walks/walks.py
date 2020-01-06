import numpy as np
import matplotlib.pyplot as plt


num_steps = 1000                                      # Setting up the numbers of walks and  
num_walks = 2000                                      # steps for each of walk               

x_final = np.zeros(num_walks)                         # Declaration of arrays for storing data  
y_final = np.zeros(num_walks)
displacement = np.zeros(num_walks)
    
plt.figure()

for i in range(0, num_walks):                            # Modeling a number of walks using a loop 
    x = 2 * (np.random.random(num_steps) > 0.5) - 1      # (also could be done using vectorizing, but it's complicated)
    y = 2 * (np.random.random(num_steps) > 0.5) - 1      # Getting arrays of only 1 and -1
    x_pos = np.cumsum(x)
    y_pos = np.cumsum(y)
    if i < 4:                                            # Drawing only 4 first "walks"
        plt.subplot(2, 2, i + 1)
        plt.plot(x_pos, y_pos)
        plt.axis('equal')
    x_final[i] = x_pos[-1]                               # Saving the info about each walk
    y_final[i] = y_pos[-1]
    displacement[i] = np.sqrt(x_final[i] ** 2 + y_final[i] ** 2)

displacement = np.power(displacement, 2)                 # Drawing the scatter plot and the histogram (logarithmic)    
plt.figure()
plt.hist(displacement, log = True)
plt.figure()
plt.scatter(x_final, y_final)
print(np.mean(displacement))                            # Printing the mean-square displacement