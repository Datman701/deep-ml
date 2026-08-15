import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	magnitude = 0
	direction = []

	for i in gradient:
		magnitude = magnitude + i**2
	
	magnitude = magnitude**0.5

	
	if(magnitude ==0):
		direction = np.zeros(len(gradient))
	
	else:
		for i in gradient:
			direction.append(i/magnitude)

	return {'magnitude':magnitude , 'direction': direction , 'descent_direction':[-1*i for i in direction]}

	# Your code here
	pass