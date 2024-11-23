import numpy as np
import matplotlib.pyplot as plt

# Parameters of the triangular distribution
a = 1    # Minimum value
b = 10   # Maximum value
c = 1    # Mode (found from mean condition)

# True mean of the distribution
true_mean = (a + b + c) / 3

# Function to generate a random variate from the triangular distribution
def triangular_random_variate():
    U = np.random.rand()  # Generate a uniform random number U in [0, 1]
    if U < (c - a) / (b - a):
        return a + np.sqrt(U * (b - a) * (c - a))
    else:
        return b - np.sqrt((1 - U) * (b - a) * (b - c))

# Generate 1000 random variates
n = 1000
random_variates = [triangular_random_variate() for _ in range(n)]

# Compute the sample mean
sample_mean = np.mean(random_variates)

# Calculate the difference between sample mean and true mean
difference = abs(sample_mean - true_mean)

# Print the results
print(f"True Mean of the distribution: {true_mean}")
print(f"Sample Mean of 1000 random variates: {sample_mean}")
print(f"Difference between Sample Mean and True Mean: {difference}")