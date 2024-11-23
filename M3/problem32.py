import numpy as np
import matplotlib.pyplot as plt

# Triangular distribution parameters

a = 2   # min
c = 5   # mode
b = 7   # max

# this is the fastest way of doing it but probably not allowed
#escort_times = np.random.triangular(a, c, b, 1000)

# Using inverse transform sampling method

U = np.random.uniform(0, 1, 1000)
escort_times = np.zeros(1000)

# Threshold to decide if U is below or above mode (this is F(c))
Fc = (c - a) / (b - a)

# Inverse transform sampling for triangular distribution
for i in range(1000):
    if U[i] <= Fc:
        # When U <= F(c)
        escort_times[i] = a + np.sqrt(U[i] * (b - a) * (c - a))
    else:
        # When U > F(c)
        escort_times[i] = b - np.sqrt((1 - U[i]) * (b - a) * (b - c))


plt.figure(figsize=(10, 6))
plt.hist(escort_times, bins=30, alpha=0.7, edgecolor='black', color='blue')
plt.title('Distribution of Escort Times (Triangular Distribution)')
plt.xlabel('Escort Time (minutes)')
plt.ylabel('amount')
plt.grid(True)
plt.show()