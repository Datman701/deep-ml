import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []

	if(mode=="row"):
		for i in matrix:
			means.append(np.mean(i))
	else:
		for i in range (len(matrix[0])):
			x = 0
			for j in range(len(matrix)):
				x = x + matrix[j][i]
			means.append(x/len(matrix))

	return means