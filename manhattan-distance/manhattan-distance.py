import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    
    if len(x)  == len(y):
        m_dis = 0
        for i in range(len(x)):
            m_dis += np.abs(x[i] - y[i])
    return float(m_dis)
    pass