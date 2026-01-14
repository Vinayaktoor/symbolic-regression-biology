import os
import numpy as np
from sbml_loader import load_sbml
from simulate_ode import simulate
from preprocess import add_noise, estimate_derivative
from symbolic_regression import run_sr
import json
# Load SBML model
rr, species, params = load_sbml("data/repressilator.xml")
print("Species:", species)

# Simulate dynamics
t, X = simulate(rr)

# Add noise
X_noisy = add_noise(X, sigma=0.02)

# Estimate derivatives
dXdt = estimate_derivative(X_noisy, t)
# Save result 
os.makedirs("results", exist_ok=True)

equations = {}
# Run symbolic regression for each species
for i, s in enumerate(species):
    print(f"\nDiscovering equation for d{s}/dt")
    model = run_sr(X_noisy, dXdt[:, i], species)
    
    best_eq = model.get_best()
    print(best_eq)

    equations[s] = best_eq
    print(model)
with open("results/recovered_equations.json", "w") as f:
    json.dump({k: str(v) for k, v in equations.items()}, f, indent=2)