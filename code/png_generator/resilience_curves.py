# Colab: Resilience curves under different scenarios
import numpy as np
import matplotlib.pyplot as plt
import os

# Crear carpeta de salida
os.makedirs("Figuras", exist_ok=True)

def logistic_R(A, Ac):
    return 1.0 / (1.0 + np.exp(-(A - Ac)))

# Escenarios (E, n) -> Ac = E/n
scenarios = [
    {"name": "Low pressure, high complexity", "E": 12, "n": 4, "color": "#1f77b4"},
    {"name": "Moderate pressure, moderate complexity", "E": 18, "n": 3, "color": "#ff7f0e"},
    {"name": "High pressure, low complexity", "E": 24, "n": 2, "color": "#2ca02c"},
]

A = np.linspace(0, 30, 400)
plt.figure(figsize=(7, 5))
for s in scenarios:
    Ac = s["E"] / s["n"]
    R = logistic_R(A, Ac)
    plt.plot(A, R, label=f"{s['name']} (Ac={Ac:.2f})", color=s["color"], linewidth=2)
    plt.axvline(Ac, color=s["color"], linestyle="--", alpha=0.6)

# Separatrices opcionales de referencia (ejemplo didáctico)
plt.axhline(0.5, color="gray", linestyle=":", linewidth=1.5, label="Transition (R=0.5)")

plt.title("Resilience curves R(A,E,n) with base threshold Ac=E/n")
plt.xlabel("Adaptive Amplitude (A)")
plt.ylabel("Resilience R(A,E,n)")
plt.ylim(0, 1)
plt.xlim(0, 30)
plt.grid(alpha=0.25)
plt.legend(loc="lower right", fontsize=9)
plt.tight_layout()
plt.savefig("Figuras/resilience_curves.png", dpi=300)
plt.show()
