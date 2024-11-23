import numpy as np
import matplotlib.pyplot as plt

data = [0.64, 0.59, 1.1, 3.3, 0.54, 0.04, 0.45, 0.25, 4.4, 2.7, 2.4, 1.1, 3.6, 0.61, 0.20, 1.0, 0.27, 1.7, 0.04, 0.34]

# we dont have the parameters for the distribution
# so we need to estimate it

mean = np.mean(data)
lambda_est = 1 / mean

x_values = np.linspace(0, max(data), 10000)  # Generate x values for plotting
#fitted_pdf = lambda_est * np.exp(-lambda_est * x_values)  # Exponential PDF formula

# Step 3: Plot the histogram of the data and the fitted distribution
plt.figure(figsize=(10, 6))
plt.hist(data, bins=10, alpha=0.7, color='orange', edgecolor='black', label='Data')

# Plot the fitted exponential PDF
#plt.plot(x_values, fitted_pdf, 'b-', lw=2, label=f'Fitted Exponential (λ = {lambda_est:.2f})')

# Add titles and labels
plt.title('Processing Time Distribution and Fitted Exponential Distribution')
plt.xlabel('Processing Time (minutes)')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()