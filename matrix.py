import numpy as np

matrix = np.array([[1,3,5,7], [2,4,6,8]])
matrix2 = np.array([[6,3,4,7], [9,8,3,2]])
scalar = 10
print ("Adding scalar to matrix: \n", matrix + scalar)
print ("Accesing elemtn at 1,1: ", matrix[1,1])
print ("Matrix multiplication: ", matrix @ matrix2.T )
print ("Interse of matrix is : ", np.linalg.inv(matrix))