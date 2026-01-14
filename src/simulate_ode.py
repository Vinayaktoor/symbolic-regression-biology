import numpy as np

def simulate(rr, t_end=50, n_points=1000):
    result = rr.simulate(0, t_end, n_points)
    t = result[:, 0]
    X = result[:, 1:]
    return t, X
