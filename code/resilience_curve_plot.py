# --- Imports ---
import numpy as np
import matplotlib.pyplot as plt

# --- Resilience Rate (Base Formula) ---
# We use the base formula R(A, E, n)
def resilience(A, E, n):
    # Ac represents the Critical Adaptive Amplitude (Ac)
    Ac = E / n
    # Logistic function: R approaches 1 as A increases past Ac
    return 1 / (1 + np.exp(-(A - Ac)))

# --- Parameters and Thresholds ---
# 1. Internal Separatrix (Reference Threshold A_c_int)
E_int = 6  # Base external pressure (Stress Factor E)
n_int = 2  # Base Complexity Factor (n)
A_c_int = E_int / n_int  # Result: 3.0

# 2. External Separatrix (Shifted Threshold A_c_ext)
# Represents a scenario of greater External Stress (E)
E_ext = 8  # Higher external pressure
n_ext = 2  # Same complexity
A_c_ext = E_ext / n_ext  # Result: 4.0

# --- Range of A Values and Curves ---
A_range = np.linspace(0, 6, 200)

# Main curve (using internal parameters)
R_values_int = resilience(A_range, E_int, n_int)

# --- Plot ---
plt.figure(figsize=(8,6))

# Logistic Curve
plt.plot(A_range, R_values_int, color="blue", linewidth=2, label="Resilience Curve $R(A, E, n)$")

# 1. Internal Separatrix (Coherence Threshold)
# The point where R=0.5 under internal conditions (E=6, n=2).
plt.axvline(x=A_c_int, linestyle="-", color="#32CD32", linewidth=2, label="Internal Separatrix ($A_{c}=3.0$)")

# 2. External Separatrix (Stress Threshold)
# The threshold the system would shift to under higher pressure (E=8, n=2).
plt.axvline(x=A_c_ext, linestyle="--", color="red", linewidth=2, label="External Separatrix ($A'_{c}=4.0$)")

# Resilience Line R=0.5
plt.axhline(y=0.5, linestyle=":", color="gray")

# State Labels
plt.text(0.5, 0.2, "Fragile State", fontsize=10)
plt.text(4.5, 0.8, "Resilient State", fontsize=10)
plt.text(3.1, 0.55, "Transition Zone", fontsize=9, color='brown')

# Axes and Title
plt.xlabel("Adaptive Amplitude (A)")
plt.ylabel("Resilience R")
plt.title("TCRT: Logistic Curve with Double Separatrix (Base Formulation)")

plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
