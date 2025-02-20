import numpy as np
import matplotlib.pyplot as plt

# Define time array (from 0 to 20 seconds)
t = np.linspace(0, 20, 100)

# Define function of x
x_t = np.exp(-0.2*t)*np.cos(0.5*t+1.2)

# Create the plot
plt.figure()
plt.plot(t, x_t, color='blue')
plt.xlabel(r'$t$')
plt.ylabel(r'Signal $x(t)$')
plt.title('example 3')
plt.xlim([0,20])
plt.ylim([-0.5,0.5])
plt.grid(True)

# Show the plot
plt.show()