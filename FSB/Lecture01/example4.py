import numpy as np
import matplotlib.pyplot as plt

# Part (a): Define the discrete signal x[n]
n_a = np.array([-3,-2,-1,0,1,2,3,4,5])
x_n = np.array([0,0,0,1,3,0,-2,2,0])

# Part (b): Define the signal f[n] = A * (alpha)^n with A=5, alpha=0.6
A = 5
alpha = -0.6
n_b = np.arange(-5,5,1) # Define n from 0 to 9
f_n = A * (alpha ** n_b)

# Create two subplots
plt.figure(figsize=(10,6))

# Subplot for part (a)
plt.subplot(2,1,1)
plt.stem(n_a, x_n, basefmt=" ")
plt.title('(a) Discrete signal $x[n]$')
plt.xlabel('$n$')
plt.ylabel('$x[n]$')
plt.xlim([-3,5])
plt.ylim([-2,3])
plt.grid(True)

# Subplot for part (b)
plt.subplot(2,1,2)
plt.stem(n_b, f_n, basefmt=" ")
plt.title('(b) $f[n]= A(alpha)^n$ with $A=5$, $alpha=-0.6$')
plt.xlabel('$n$')
plt.ylabel('$f[n]$')
plt.xlim([-5,5])
plt.ylim([-80,40])
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()
