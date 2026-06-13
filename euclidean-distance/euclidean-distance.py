import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    if len(x) == len(y):
        sq_mat = np.empty(len(x))
        for i in range(len(x)):
            sq_mat[i] = (x[i] - y[i])**2
        return (np.sum(sq_mat))**0.5
    else:
        raise ValueError
    pass