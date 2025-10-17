
#CI_Lab HW1 Setayesh Khasehtarash 
import numpy as np

# Define a 3x3 matrix M as a test
M = np.array([[1, 0, np.sin(np.pi/4)],
              [0, 1, np.sin(np.pi/4)],
              [1, 0, 1]])

# Defining sigmoid function
def sigmoid(x):
    # Calculating the sigmoid value for input x
    return 2 / (1 + np.exp(-x)) - 1

# Defining the derivative of the sigmoid function
def derivative_of_sigmoid(x):
    # Calculating the derivative of the sigmoid value for input x
    return (1 - np.square(sigmoid(x))) / 2

# Defining the tanh function for a matrix
def tanh(Matrix, n, m):
    Sum = 0
    
    # Iterating over each element in the matrix
    for i in range(n):
        for j in range(m):
            # Calculating the tanh value for each element and addng it to the sum
            Sum += (np.exp(Matrix[i, j]) - np.exp(-Matrix[i, j])) / (np.exp(Matrix[i, j]) + np.exp(-Matrix[i, j]))
    return Sum

# Defining the sigmatrix function to calculate the sum of sigmoid and its derivative for each element in the matrix
def sigmatrix(Matrix, n, m):
    Sum1 = 0
    Sum2 = 0
    
    # Iterating over each element in the matrix
    for i in range(n):
        for j in range(m):
            # Calculating the sigmoid value and add it to Sum1
            Sum1 += sigmoid(Matrix[i, j])
            # Calculating the derivative of sigmoid value and add it to Sum2
            Sum2 += derivative_of_sigmoid(Matrix[i, j])
    return Sum1, Sum2

# Getting the shape of the matrix M
(n, m) = np.shape(M)

# Calling the sigmatrix function to get the sums of sigmoid and its derivative
sum1, sum2 = sigmatrix(M, n, m)
# Calling the tanh function to get the sum of tanh values
sum3 = tanh(M, n, m)

# Printing the results
print("Result of sigmoid sum is= " + str(sum1))
print("Result of derivative of sigmoid sum is = " + str(sum2))
print("Result of tanh sigmoid sum is= " + str(sum3))
