# Colab: State map by coherence ratio
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("Figuras", exist_ok=True)

rho = np.linspace(0, 2.0, 400)
rho_c = 1.0  # ejemplo didáctico

plt.figure(figsize=(7, 4))

# Rellenos por región
plt.fill_between(rho, 0, 1, where=(rho < rho_c), color="#1f77b4", alpha=0.12, label="Fragility (ρ < ρc)")
plt.fill_between(rho, 0, 1, where=(rho > rho_c), color="#d62728", alpha=0.12, label="Collapse (ρ > ρc)")

# Separatrix
plt.axvline(rho_c, color="#ff7f0e", linestyle="--", linewidth=2, label="Internal Separatrix (ρ = ρc)")

plt.title("State map by coherence ratio ρ relative to ρc")
plt.xlabel("ρ = F / K (Coherence Ratio)")
plt.ylabel("State indicator (schematic)")
plt.yticks([])
plt.xlim(0, 2.0)
plt.grid(alpha=0.25)
plt.legend(loc="upper right", fontsize=9)
plt.tight_layout()
plt.savefig("Figuras/state_map.png", dpi=300)
plt.show()
