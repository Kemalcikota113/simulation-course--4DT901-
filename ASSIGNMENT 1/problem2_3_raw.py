import numpy as np
import matplotlib.pyplot as plt  # Use this for histogram plotting

print('1000 Uniform random numbers:')
def generate_random_variate():
    # generate a uniform random number between 0 and 1 manually
    U = np.random.uniform(0, 1)

    print(U)

    if U <= 0.25:
        return 2 + 2 * np.sqrt(U)
    else:
        return 6 - 2 * np.sqrt(3 - (3*U))


# Generate 1000 random numbers and append them to the list ranVars
randVars = []

for i in range(1000):  
    randVars.append(generate_random_variate())


# main
print('Array of 1000 random variates:')
print(randVars)

# Plot the histogram
plt.hist(randVars, bins=30, alpha=0.6, color='blue')
plt.grid()

plt.title("Histogram of 1000 Random Variates")
plt.xlabel("Random Variates")
plt.ylabel("Frequency of values")

plt.show()
