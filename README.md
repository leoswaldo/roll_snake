# Roll Snake

### Problem Description
Given a square matrix of integer numbers, write a function that prints the
matrix to the standard output(stdout) on a single line starting in the
upper-left corner and continuing clockwise, in circles, from the exterior
towards interior.

> Note that your function will receive the following arguments:
> - matrix: which is an array of integers giving the matrix as follows. The
> first width elements in the array represent the first line of the matrix,
> the next width elements represent the second line of the matrix and so on.
> - width: which is an integer value giving the width of the square matrix

### Data contraints
The width values will not exceed 250
All elements in the matrix are integer numbers in the following rnage[1, 2^31-1]

###Efficiency contraints
Your function is expected to print the result in less than 2 seconds

### Example
Input: matrix = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], width = 4

Output: [1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10]

### Explanation
 1 2 3 4
 5 6 7 8
 9 10 11 12
 13 14 15 16

### Other Solutions found
https://github.com/harmonymeow/Practice/blob/master/snake.rb