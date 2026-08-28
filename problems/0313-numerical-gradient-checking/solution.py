import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """

    d = []

    for i in range(len(x)): 
        e = np.zeros_like(x)
        e[i]  = 1
        d.append((f(x + epsilon*e) - f(x - epsilon*e)) / (2*epsilon))

    diff = np.linalg.norm(analytical_grad - d) / (np.linalg.norm(d) + np.linalg.norm(analytical_grad))

    return (d , diff)