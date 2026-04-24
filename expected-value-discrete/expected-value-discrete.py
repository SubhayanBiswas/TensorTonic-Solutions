import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)
    count = 0
    for i in range(len(p)):
        if p[i] <= 1 and p[i] >=0:
            count += 1
    if count == len(p) and np.sum(p)==1:
        return np.dot(x, p)
    else:
        raise ValueError
    pass
