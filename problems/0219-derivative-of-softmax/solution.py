import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	m = sum(np.exp(i) for i in x)
	s = [np.exp(i)/m for i in x]
	ans = []
	for i in range (len(x)):
		y = []
		for j in range(len(x)):
			if(i==j):
				y.append(s[i]*(1 - s[j]))
			else:
				y.append(-s[i]*s[j])
		ans.append(y)
	return ans
	# Your code here
	pass