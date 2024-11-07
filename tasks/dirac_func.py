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




x_values = np.linspace(-5, 10, 500)

# Plot the integrand for each sigma
plt.figure(figsize=(10, 6))
for sigma in sigma_values:
    y_values = integrand(x_values, sigma)
    plt.plot(x_values, y_values, label=f'sigma = {sigma}')

# Add titles and labels
plt.title('Integrand Function for Different Sigma Values')
plt.xlabel('x')
plt.ylabel('f(x, sigma)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
