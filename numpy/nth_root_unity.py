import numpy as np

# Function to calculate nth roots of unity
def nth_roots_of_unity(n):
    # Initialize an empty list to store the roots
    roots = []
    
    # Loop through k from 0 to n-1
    for k in range(n):
        # Use Euler's formula: e^(2*pi*i*k/n)
        # np.exp() calculates the exponential, and 2j*np.pi*k/n gives the angle in radians
        root = np.exp(2j * np.pi * k / n)
        
        # Append each root to the list
        roots.append(root)
    
    return roots

# Compute nth roots of unity for n = 2, 3, and 4
roots_n2 = nth_roots_of_unity(2)
roots_n3 = nth_roots_of_unity(3)
roots_n4 = nth_roots_of_unity(4)

print("Roots of unity for n=2:", roots_n2)
print("Roots of unity for n=3:", roots_n3)
print("Roots of unity for n=4:", roots_n4)
