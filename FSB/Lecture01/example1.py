import numpy as np
import matplotlib.pyplot as plt

# Time array (from 0 to 1 second, 1000 points)
t = np.linspace(0, 1, 1000)

# Sinusoial signals
signal1 = np.sin(2 * np.pi * 2*t) # First signal: standard sine wave
signal2 = 0.5 * np.cos(2 * np.pi * 5*t - np.pi/4) # Second signal:

# Create the plot
plt.figure()
plt.plot(t, signal1, label='Signal 1')
plt.plot(t, signal2, 'k--', label='Signal 2') 
plt.title('Test plots of sninusoids')
plt.xlabel('Time (sec.)')
plt.ylabel('Signal amplitudes')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


