# Python3 program to print all elements
# of given matrix in diagonal order
ROW = 50
COL = 4

# Main function that prints given
# matrix in diagonal order


def diagonalOrder(matrix):

	# There will be ROW+COL-1 lines in the output
	for line in range(1, (ROW + COL)):
		# Get column index of the first element
		# in this line of output. The index is 0
		# for first ROW lines and line - ROW for
		# remaining lines
		start_col = max(0, line - ROW)

		# Get count of elements in this line.
		# The count of elements is equal to
		# minimum of line number, COL-start_col and ROW
		count = min(line, (COL - start_col), ROW)
		count
		# Print elements of this line
		for j in range(0, count):
			print(matrix[min(ROW, line) - j - 1]
						[start_col + j], end="\t")

		print()


# Utility function to print a matrix
def printMatrix(matrix):
	for i in range(0, ROW):
		for j in range(0, COL):
			print(matrix[i][j], end="\t")

		print()


# Driver Code
M = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16],
	[17, 18, 19, 20]]
print("Given matrix is ")
printMatrix(M)

print("\nDiagonal printing of matrix is ")
diagonalOrder(M)

# This code is contributed by Nikita Tiwari.

# Python3 program to print all elements
# of given matrix in diagonal order
R = 5
C = 4


def isValid(i, j):
	if (i < 0 or i >= R or j >= C or j < 0):
		return False
	return True


def diagonalOrder1(arr):

	# through this for loop we choose each element
	# of first column as starting point and print
	# diagonal starting at it.
	# arr[0][0], arr[1][0]....arr[R-1][0]
	# are all starting points
	for k in range(0, R):
		print(arr[k][0], end=" ")

		# set row index for next point in diagonal
		i = k - 1

		# set column index for next point in diagonal
		j = 1

		# Print Diagonally upward
		while (isValid(i, j)):
			print(arr[i][j], end=" ")
			i -= 1
			j += 1 # move in upright direction

		print()

	# Through this for loop we choose each
	# element of last row as starting point
	# (except the [0][c-1] it has already been
	# processed in previous for loop) and print
	# diagonal starting at it.
	# arr[R-1][0], arr[R-1][1]....arr[R-1][c-1]
	# are all starting points

	# Note : we start from k = 1 to C-1;
	for k in range(1, C):
		print(arr[R-1][k], end=" ")

		# set row index for next point in diagonal
		i = R - 2

		# set column index for next point in diagonal
		j = k + 1

		# Print Diagonally upward
		while (isValid(i, j)):
			print(arr[i][j], end=" ")
			i -= 1
			j += 1 # move in upright direction

		print()


# Driver Code
arr = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16],
	[17, 18, 19, 20]]

# Function call
diagonalOrder1(arr)

# This code is contributed by Nikita Tiwari.

diagonalOrder(arr)