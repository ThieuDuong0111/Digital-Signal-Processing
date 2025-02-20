import numpy as np
import matplotlib.pyplot as plt

# Define time array (from 0 to 7 seconds)
t = np.linspace(0,2*np.pi, 1000)

# Damped sinusoidal function
A = 10 # Amplitude 1
B = 20 # Amplitude 2
a = 0.5 # Damping factor 1
b= 1 # Damping factor 2
omega1 = 4*np.pi # Angular frequency
omega2 = 2*np.pi # Angular frequency 2
x_t = A * np.exp(-a * t) * np.sin(omega1 * t) + B * np.exp(-b*t) * np.sin(omega2 * t)

plt.figure()
plt.plot(t, x_t, color='blue')
plt.xlabel(r'$t(s)$')
plt.ylabel(r'Signal $x(t)$')
plt.title('(a)')
plt.xlim([0,7])
plt.ylim([-15,25])
plt.grid(True)

# Show the plot
plt.show()