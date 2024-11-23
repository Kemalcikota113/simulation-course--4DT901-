import numpy as np
import matplotlib.pyplot as plt

def milkiness_cdf(x):

    # CDF --> Log distribution
    return 1 / (1 + np.exp(-1.5 * (x - 3)))


def inverse_transform_sampling(cdf, num_samples=1000):

    uniform_samples = np.random.uniform(0, 1, num_samples)      # U ~ U(0, 1) sample

    milkiness_values = np.array([binary_search_for_milkiness(cdf, u) for u in uniform_samples])     # inverse CDF
    return milkiness_values


def binary_search_for_milkiness(cdf, target, tol=1e-4):     # BS

    low, high = 1, 5 # Range of milkiness

    while high - low > tol:
        mid = (low + high) / 2
        if cdf(mid) < target:
            low = mid
        else:
            high = mid
    return (low + high) / 2

# Step 3: Generate milkiness values
num_samples = 1000
milkiness_values = inverse_transform_sampling(milkiness_cdf, num_samples)

# Step 4: Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(milkiness_values, bins=30, density=True, alpha=0.6, color='skyblue')
plt.title("Distribution of Milkiness Levels per Glass of Milk")
plt.xlabel("Milkiness Level")
plt.ylabel("Density")
plt.grid(True)
plt.show()
