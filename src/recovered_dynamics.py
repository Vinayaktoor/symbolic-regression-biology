import numpy as np

def recovered_system(t, state):
    X, Y, Z = state

    # Replace these with your recovered equations
    dXdt = 2.31 - Y*Z
    dYdt = 1.53 - Y
    dZdt = 2.31 - Y*Z

    return [dXdt, dYdt, dZdt]
