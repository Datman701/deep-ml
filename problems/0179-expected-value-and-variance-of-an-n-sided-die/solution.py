import numpy as np

def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	ex = np.sum([i for i in range(1,n+1)])/n
	ex2 = np.sum([i**2 for i in range(1,n+1)])/n
	return(ex , ex2 - ex**2)
	pass