import numpy as np

def add_noise(X, sigma=0.01):
    noise = sigma * np.random.randn(*X.shape)
    return X + noise

def estimate_derivative(X, t):
    dXdt = np.gradient(X, t, axis=0)
    return dXdt
