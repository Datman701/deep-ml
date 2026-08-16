import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    values , count = np.unique(samples , return_counts=True)

    x = np.sum(count)

    ans = []

    for i in range(len(values)):
        ans.append((values[i],count[i]/x))
    # TODO: Implement the function
    return ans