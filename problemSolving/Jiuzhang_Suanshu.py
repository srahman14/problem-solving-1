#  Jiuzhang suanshu
# The Nine Chapters on the Mathematical Art

# Problem Description:
# Three fruits: Apple, Orange and Grape are mixed in three different containers to produce juice blends
# The total volume of each container is known -> Task is to determine the volumes of Apple, Orange, Grape

# First container contains: 3 parts of Apple, 2 parts of Orange, and 1 part of Grape. The total volume is 60 ml.
# Second container contains: 1 part of Apple, 3 parts of Orange, and 2 parts of Grape. The total volume is 50 ml.
# Third container contains: 2 parts of Apple, 1 part of Orange, and 2 parts of Grape. The total volume is 40 ml.

# This will be needed when creating matrices for X,Y,Z with the constants
from copy import deepcopy

# Matrix of Coefficients -> corresponds to the parts of Apple/Orange/Grape
matrix = [[3, 2, 1],
          [1, 3, 2],
          [2, 1, 2]]
# Constants -> known values for the container (ml)
constants = [60, 50, 40]

# Set a1, b1, c1...c3 to every corresponding value in matrix
a1, b1, c1 = matrix[0][0], matrix[0][1], matrix[0][2]
a2, b2, c2 = matrix[1][0], matrix[1][1], matrix[1][2]
a3, b3, c3 = matrix[2][0], matrix[2][1], matrix[2][2]

# Formula given to calculate the determinant of the coefficents
determinant = (a1 * b2 * c3) - (a1 * c2 * b3) + (b1 * c2 * a3) - \
    (b1 * a2 * c3) + (c1 * a2 * b3) - (c1 * b2 * a3)

# Create deepcopies for the matrices to construct new compound object
# This is slower than a shallow copy, however necessary here, as the matrices need to be created uniquely
# Matrix X corresponds to Apple, Matrix Y corresponds to Orange and Matrix Z corresponds to Grape
matrixX = deepcopy(matrix)
matrixY = deepcopy(matrix)
matrixZ = deepcopy(matrix)

# Input the values of the constants in the corresponding matrices, X, Y, Z
matrixX[0][0],  matrixX[1][0],  matrixX[2][0] = constants[0], constants[1], constants[2]
matrixY[0][1],  matrixY[1][1],  matrixY[2][1] = constants[0], constants[1], constants[2]
matrixZ[0][2],  matrixZ[1][2],  matrixZ[2][2] = constants[0], constants[1], constants[2]

# Once again use a1,b1,c1...c3 to match to every value in the matrix of X
a1, b1, c1 = matrixX[0][0], matrixX[0][1], matrixX[0][2]
a2, b2, c2 = matrixX[1][0], matrixX[1][1], matrixX[1][2]
a3, b3, c3 = matrixX[2][0], matrixX[2][1], matrixX[2][2]

# Use the same formula to solve for the determinat of X
determinantX = (a1 * b2 * c3) - (a1 * c2 * b3) + (b1 * c2 * a3) - \
    (b1 * a2 * c3) + (c1 * a2 * b3) - (c1 * b2 * a3)

# Once again use a1,b1,c1...c3 to match to every value in the matrix of Y
a1, b1, c1 = matrixY[0][0], matrixY[0][1], matrixY[0][2]
a2, b2, c2 = matrixY[1][0], matrixY[1][1], matrixY[1][2]
a3, b3, c3 = matrixY[2][0], matrixY[2][1], matrixY[2][2]

# Use the same formula to solve for the determinat of Y
determinantY = (a1 * b2 * c3) - (a1 * c2 * b3) + (b1 * c2 * a3) - \
    (b1 * a2 * c3) + (c1 * a2 * b3) - (c1 * b2 * a3)

# Once again use a1,b1,c1...c3 to match to every value in the matrix of Z
a1, b1, c1 = matrixZ[0][0], matrixZ[0][1], matrixZ[0][2]
a2, b2, c2 = matrixZ[1][0], matrixZ[1][1], matrixZ[1][2]
a3, b3, c3 = matrixZ[2][0], matrixZ[2][1], matrixZ[2][2]

# Use the same formula to solve for the determinat of Y
determinantZ = (a1 * b2 * c3) - (a1 * c2 * b3) + (b1 * c2 * a3) - \
    (b1 * a2 * c3) + (c1 * a2 * b3) - (c1 * b2 * a3)

# Use the final formula of diving the determinants by the determinant of coefficients to get
# the unkonwn variable
x = determinantX / determinant
y = determinantY / determinant
z = determinantZ / determinant

# Use round to round to 2 decimal places
print("Solution for X: ", round(x, 2))
print("Solution for Y: ", round(y, 2))
print("Solution for Z: ", round(z, 2))
