import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	m = max(scores)
	s = sum([np.exp(i - m) for i in scores])

	return [np.log(np.exp(i - m)/s) for i in scores]