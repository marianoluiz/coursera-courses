import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)

# Access the element on the second row and third column

""" 
its gonna be like

A[0,0] A[0,1] A[0,2]
A[1,0] A[1,1] A[1,2]
A[2,0] A[2,1] A[2,2]

"""

# Access the element on the second row and third column

A[1, 2]
# a[ROW, COLN]
# [[00, 01, 02], [10, 11, 12]]

# Access the element on the second row and third column

A[1][2]
# a[ROW, COLN]
# [[00, 01, 02], [10, 11, 12]]


# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 

# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 

# Add X and Y: MATRIX ADDITION

Z = X + Y