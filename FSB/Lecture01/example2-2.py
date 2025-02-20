import numpy as np
import matplotlib.pyplot as plt

# Define time array (from 0 to 5 seconds)
t = np.linspace(0, 5, 50)

# Define unit step function (Heaviside step function)
u_t = np.heaviside(t - 1, 1) # Step at t=1, output 1 for t >= 1

# Create the plot
plt.figure()
plt.plot(t, u_t, color='blue')
plt.xlabel(r'$t$')
plt.ylabel(r'Signal $u(t)$')
plt.title('(b)')
plt.xlim([0,5])
plt.ylim([0,1.2])
plt.grid(True)

# Show the plot
plt.show()