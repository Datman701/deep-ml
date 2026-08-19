import torch

def grad_of_quadratic(x_value: float) -> float:
    # TODO: build a tracked leaf for x, compute f(x), run backprop, return df/dx as a float
    a = torch.tensor(x_value , requires_grad=True)
    y = a**2 + 3*a + 2
    y.backward()
    return float(a.grad)
