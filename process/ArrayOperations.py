import numpy as np

# Create 1D and 2D arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])

print(arr1)
print(arr2)

# Arithmetic
print(arr1 + 10)           # Add 10 to each element
print(arr1 * 2)            # Multiply each element by 2

# Stats
print("Mean:", arr1.mean())
print("Sum:", arr1.sum())
