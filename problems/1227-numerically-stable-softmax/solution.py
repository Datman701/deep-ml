import torch

def softmax(t, dim):
    """Numerically stable softmax along dim.

    Args:
        t (torch.Tensor): input tensor
        dim (int): dimension along which to apply softmax

    Returns:
        torch.Tensor: tensor of same shape as t; slices along dim sum to 1
    """
    a = t.max(dim=dim,keepdim=True).values
    b = t - a
    c = b.exp()
    d = c.sum(dim=dim,keepdim=True)

    return c/d





    # TODO: subtract max along dim, exp, then normalize
    pass
