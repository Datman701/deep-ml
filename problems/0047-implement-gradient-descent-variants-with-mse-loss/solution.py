import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """

    for i in range(n_epochs):

        if(method == 'batch'):
            error = X @ weights - y
            w_grad = ((X.T @ error) / len(X)) * 2

            weights = weights - learning_rate * w_grad

        elif(method == 'mini_batch'):
            j = 0
            while j < len(X):
                x = X[j : batch_size + j , :]
                error = x @ weights - y[j : batch_size + j]
                w_grad = ((x.T @ error) / len(x))*2

                weights = weights - learning_rate * w_grad
                j = j + batch_size

        else:
            for j in range(len(X)):
                error = X[j] @ weights.T - y[j]
                w_grad = (X[j].T * error)*2

                weights = weights - learning_rate * w_grad
    return weights




