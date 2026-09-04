def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""

	x = [row[:] for row in matrix]

	for i in range(len(x[0])):
		for j in range (i+1 , len(x)):
			multiplier = x[j][i] / x[i][i]
			for k in range(i + 1 , len(x[0])):
				x[j][k] = x[j][k] - multiplier * x[i][k]

	det = 1
	for i in range(len(x[0])):
		det = det * x[i][i]

	tr = 0
	for i in range(len(matrix[0])):
		tr = tr + matrix[i][i]

	# Your code here
	return (det , tr)