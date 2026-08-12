def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    ans = []
    for i in range(len(a[0])):
        x = []
        for j in range(len(a)):
            x.append(a[j][i])
        ans.append(x)
    return ans

    # Your code here
    pass