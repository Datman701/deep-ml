import math

def sigmoid( z: float) -> float:
	x = math.exp(-z)
	return 1/(1 + x)

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
	error = []
	for i in range(len(features)):
		z = sum(x * y for x,y in zip(features[i],weights)) + bias
		p = sigmoid(z)
		probabilities.append(p)
		error.append(math.pow(p - labels[i],2))
	

	return probabilities, sum(error)/len(error)