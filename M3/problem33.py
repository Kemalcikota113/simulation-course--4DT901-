# using the hint from the answer sheet and using
# normal distributions

import numpy as np
import matplotlib.pyplot as plt

# A12117c
mean_A = 2
std_dev_A = 0.4  # 20%

# B33433x
mean_B = 3.0
std_dev_B = 0.6  # 20%

times_A = np.random.normal(mean_A, std_dev_A, 100000)
times_B = np.random.normal(mean_B, std_dev_B, 100000)



# Plot the distribution of operation times for both types
plt.figure(figsize=(10, 6))

# Plot for Type A12117c
plt.hist(times_A, bins=30, alpha=0.7, label='Type A12117c', edgecolor='black', color='blue')

# Plot for Type B33433x
plt.hist(times_B, bins=30, alpha=0.7, label='Type B33433x', edgecolor='black', color='orange')

plt.title('Distribution of Operation Times for Insertion/Sealing/Inspection (Normal Distribution)')
plt.xlabel('Operation Time (minutes)')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
