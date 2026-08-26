import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	mse_values = []
	updated_weights = initial_weights
	updated_bias = initial_bias
	for i in range (epochs):
		z = features @ updated_weights + updated_bias
		pred = 1 / (1 + np.exp(-z))
		error = pred - labels
		mse_values.append(round(np.mean(error**2),4))
		delta = 2/len(features) * (pred  - labels) * pred * (1 - pred)
		d_w = features.T @ delta
		d_d = np.sum(delta)
		updated_weights = updated_weights  - learning_rate * d_w
		updated_bias = updated_bias  - learning_rate * d_d

	return [round(i,4) for i in updated_weights], round(updated_bias,4),mse_values