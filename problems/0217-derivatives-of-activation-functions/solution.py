import numpy as np

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	a=0.0
	if x>0:
		a = 1.0
	y = 1 / (1 + np.exp(-x))
	return {"sigmoid":y*(1 - y),
	"tanh": 1 - np.tanh(x)**2 , "relu":a}
	pass