# Colab: Cross-system interaction map (External Separatrix)
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("Figuras", exist_ok=True)

# Parámetros de los dos sistemas (E, n)
E1, n1 = 24, 3   # sistema 1
E2, n2 = 30, 5   # sistema 2

Ac1 = E1 / n1
Ac2 = E2 / n2

A = np.linspace(0, 30, 400)

def logistic_R(A, Ac):
    return 1.0 / (1.0 + np.exp(-(A - Ac)))

R1 = logistic_R(A, Ac1)
R2 = logistic_R(A, Ac2)

plt.figure(figsize=(7, 5))
plt.plot(A, R1, color="#1f77b4", linewidth=2, label=f"System 1 (Ac1={Ac1:.2f})")
plt.plot(A, R2, color="#2ca02c", linewidth=2, label=f"System 2 (Ac2={Ac2:.2f})")

# Líneas verticales en los umbrales
plt.axvline(Ac1, color="#1f77b4", linestyle="--", alpha=0.7)
plt.axvline(Ac2, color="#2ca02c", linestyle="--", alpha=0.7)

# Región de convergencia (external separatrix ilustrativa)
delta = abs(Ac1 - Ac2)
xmin, xmax = min(Ac1, Ac2), max(Ac1, Ac2)
plt.axvspan(xmin, xmax, color="#ff7f0e", alpha=0.12, label=f"Threshold convergence (Δ={delta:.2f})")

plt.title("Cross-system interaction map: threshold convergence")
plt.xlabel("Adaptive Amplitude (A)")
plt.ylabel("Resilience R(A)")
plt.ylim(0, 1)
plt.xlim(0, 30)
plt.grid(alpha=0.25)
plt.legend(loc="lower right", fontsize=9)
plt.tight_layout()
plt.savefig("Figuras/interaction_map.png", dpi=300)
plt.show()
