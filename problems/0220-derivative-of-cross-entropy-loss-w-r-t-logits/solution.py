import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	x = sum(np.exp(logit) for logit in logits)
	softmax = [np.exp(logit) / x for logit in logits]

	softmax[target] = softmax[target] - 1

	return softmax
	# Your code here
	pass