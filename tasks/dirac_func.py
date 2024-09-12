import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the function to integrate
def integrand(x, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma**2)) * np.exp(-((x - 2)**2) / (2 * sigma**2)) * (x + 3)

# Define a function to compute the integral for a given sigma
def compute_integral(sigma):
    result, _ = quad(integrand, -np.inf, np.inf, args=(sigma))
    return result

# Define sigma values
sigma_values = [1, 0.1, 0.01]

# Compute the integrals for each sigma
integral_values = [compute_integral(sigma) for sigma in sigma_values]

# Print the results
for sigma, integral_value in zip(sigma_values, integral_values):
    print(f"Integral for sigma = {sigma}: {integral_value}")
