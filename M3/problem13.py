import numpy as np
from scipy.optimize import minimize

data = [7.936, 5.224, 3.937, 6.513,
        4.599, 7.563, 7.172, 5.132,
        5.259, 2.759, 4.278, 2.696,
        6.212, 2.407, 1.857, 5.002,
        4.612, 2.003, 6.908, 3.326]

def neg_log_likelihood(params, data):
    alpha, beta = params
    n = len(data)
    term1 = n * np.log(alpha) - n * alpha * np.log(beta)
    term2 = (alpha - 1) * np.sum(np.log(data))
    term3 = -np.sum((data / beta) ** alpha)
    return -(term1 + term2 + term3)  # Return negative for minimization

# Initial guesses for alpha and beta
initial_params = [1.0, 1.0]

# Minimize the negative log-likelihood
result = minimize(neg_log_likelihood, initial_params, args=(data,), method='L-BFGS-B',
                  bounds=((1e-6, None), (1e-6, None)))

# Extract the MLE estimates
alpha_hat, beta_hat = result.x

# Output the results
print(f"Estimated alpha (shape parameter): {alpha_hat:.4f}")
print(f"Estimated beta (scale parameter): {beta_hat:.4f}")