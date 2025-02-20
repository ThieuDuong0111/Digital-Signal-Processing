import numpy as np
import matplotlib.pyplot as plt

# Define n (from 0 to 32, inclusive)
n = np.arange(0, 32, 1)

# Define x[n]
x_n = 10*np.sin(2*np.pi*n/16)

# Create the plot
plt.figure(figsize=(8,6))
plt.stem(n, x_n, basefmt=" ")
plt.xlabel(r'$n$')
plt.ylabel(r'$x[n]$')
plt.title('(a) Discrete signal $x[n]$')
plt.xlim([0,35])
plt.ylim([-12,12])
plt.grid(True)

# Show the plot
plt.show()