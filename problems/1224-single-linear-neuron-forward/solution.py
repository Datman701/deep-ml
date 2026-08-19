import torch
import torch.nn as nn


def single_neuron_forward(x):
    """Forward pass of one fixed linear neuron.

    Args:
        x: torch.Tensor of shape (1, 3).

    Returns:
        Python float, the neuron output.
    """
    with torch.no_grad():
        w = torch.tensor([[0.5,-0.2,0.3]])
        b = torch.tensor(0.1)
        return float(x @ w.T + b)
    # TODO: build nn.Linear(3, 1), set fixed weight/bias under no_grad, return float output
    pass
