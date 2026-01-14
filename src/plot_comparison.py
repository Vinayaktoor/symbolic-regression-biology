import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from simulate_ode import simulate
from sbml_loader import load_sbml
from recovered_dynamics import recovered_system

# True system
rr, species, _ = load_sbml("data/repressilator.xml")
t_true, X_true = simulate(rr)

# Recovered system
t_span = (t_true[0], t_true[-1])
y0 = X_true[0]

sol = solve_ivp(
    recovered_system,
    t_span,
    y0,
    t_eval=t_true
)

# Plot
for i, s in enumerate(species):
    plt.figure()
    plt.plot(t_true, X_true[:, i], label="True", linewidth=2)
    plt.plot(sol.t, sol.y[i], "--", label="Recovered")
    plt.xlabel("Time")
    plt.ylabel(s)
    plt.legend()
    plt.title(f"{s}: True vs Recovered Dynamics")
    plt.show()
