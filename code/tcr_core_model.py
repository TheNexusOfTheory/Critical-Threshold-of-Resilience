# --- Import libraries ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Resilience Function ---
def resilience(A, E, n):
    Ac = E / n
    return 1 / (1 + np.exp(-(A - Ac)))

# --- Sensitivity Derivatives ---
def dR_dA(A, E, n):
    R = resilience(A, E, n)
    return R * (1 - R)

def dR_dE(A, E, n):
    R = resilience(A, E, n)
    return -(1/n) * R * (1 - R)

def dR_dn(A, E, n):
    R = resilience(A, E, n)
    return (E / n**2) * R * (1 - R)

# --- Example values (matches Table 1) ---
A_values = [14, 24, 13, 12, 5]
E_values = [26, 39, 34, 30, 27]
n_values = [2, 2, 4, 3, 4]

results = []
for A, E, n in zip(A_values, E_values, n_values):
    R = resilience(A, E, n)
    dA = dR_dA(A, E, n)
    dE = dR_dE(A, E, n)
    dn = dR_dn(A, E, n)
    results.append([A, E, n, round(R, 2), round(dA, 3), round(dE, 3), round(dn, 3)])

# DataFrame definition
col_names = ["A", "E", "n", "R", "dR/dA", "dR/dE", "dR/dn"]
df = pd.DataFrame(results, columns=col_names)
print(df)

A_vals = np.linspace(0, 30, 200)
E_val, n_val = 26, 2 
R_vals = [resilience(A, E_val, n_val) for A in A_vals]

plt.figure(figsize=(7,5))
plt.plot(A_vals, R_vals, label=f"E={E_val},n={n_val}", color="blue") 
plt.axvline(x=E_val/n_val, ls="--", color="red", label="Ac") 
plt.axhline(y=0.5, ls=":", color="gray")

plt.xlabel("A") 
plt.ylabel("R")
plt.title("TCRT Curve") 
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
