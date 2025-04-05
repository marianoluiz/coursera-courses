""" 
Numpy: library for numerical computing.
"""

import numpy as np

a = np.array([0,1,2,3,4])

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print()
print(type(a), a.dtype)

# changing val
a[0] = 0

# Slicing the numpy array
  # The element at end index is not being included in the output.
print('\nslicing: ', a[1:3])

  # [start:end:step]
print(a[1:5:2])
print(a[0:])

# Get the size of numpy array

print(a.size)

# Get the number of dimensions of numpy array

print(a.ndim)

# Get the shape/size of numpy array

print(a.shape)

# Get the mean of numpy array

mean = a.mean()

# Get the standard deviation of numpy array

standard_deviation=a.std()

# Get the biggest value in the numpy array

max_a = a.max()

# Get the smallest value in the numpy array

min_a = a.min()