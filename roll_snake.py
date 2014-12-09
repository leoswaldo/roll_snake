#!/python3/bin/python3

# Given a square matrix of integer numbers, write a function that prints the
# matrix to the standard output(stdout) on a single line starting in the
# upper-left corner and continuing clockwise, in circles, from the exterior
# towards interior.
#
# Note that your function will receive the following arguments:
# - matrix: which is an array of integers giving the matrix as follows. The
# first width elements in the array represent the first line of the matrix,
# the next width elements represent the second line of the matrix and so on.
# - width: which is an integer value giving the width of the square matrix
#
# Data contraints
# The width values will not exceed 250
# All elements in the matrix are integer numbers in the following rnage[1, 2^31-1]
#
# Efficiency contraints
# Your function is expected to print the result in less than 2 seconds
#
# Example
# Input: matrix = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], width = 4
# Output: [1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10]
#
# Explanation
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# Test scenarios

matrix = [str(n) for n in range(1, 37)]
matrix_width = 6
'''
matrix = [str(n) for n in range(1, 26)]
matrix_width = 5
'''
position = 0
snake_output = ''

# We'll iterate just a half, since there is one way to the right(i) and one
# way the left, that make us itereate the half. (plus one in case the width
# is an odd number)
matrix_width_limit = int((matrix_width / 2) + 1)

for i in range(1, matrix_width_limit + 1):
    #right
    position = (i * matrix_width) - matrix_width + (i - 1)
    for j in range(0, matrix_width - ((i - 1) * 2)):
        snake_output += (" " + matrix[position + j])

    #down
    position = (i * matrix_width) - i
    for j in range(0, matrix_width - ((i - 1) * 2) - 1):
        snake_output += (" " + matrix[position + ((j + 1) * matrix_width)])

    #left
    position = (matrix_width * matrix_width) -\
        (matrix_width * (i - 1)) - i
    for j in range(0, matrix_width - ((i - 1) * 2) - 1):
        snake_output += (" " + matrix[position - (j + 1)])

    #up
    position = (matrix_width * matrix_width) -\
        (i * matrix_width) + (i - 1)
    for j in range(0, matrix_width - (i * 2)):
        snake_output += (" " + matrix[position - ((j + 1) * matrix_width)])

#finally we print the snake
print(snake_output)