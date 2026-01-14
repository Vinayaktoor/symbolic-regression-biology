from pysr import PySRRegressor

def run_sr(X, y, variable_names):
    model = PySRRegressor(
        niterations=1000,
        binary_operators=["+", "-", "*"],
        unary_operators=[],
        elementwise_loss="loss(x, y) = (x - y)^2",
        model_selection="best",
        verbosity=0
    )
    model.fit(X, y, variable_names=variable_names)
    return model
