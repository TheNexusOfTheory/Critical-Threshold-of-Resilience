# --- Imports ---
import numpy as np
import matplotlib.pyplot as plt

# --- Tasa de Resiliencia (Fórmula Base) ---
# Usamos la fórmula base R(A, E, n)
def resilience(A, E, n):
    Ac = E / n
    return 1 / (1 + np.exp(-(A - Ac)))

# --- Parámetros y Umbrales ---
# 1. Separatriz Interna (Umbral de referencia A_c_int)
E_int = 6  # Presión externa base
n_int = 2  # Complejidad base
A_c_int = E_int / n_int  # Resultado: 3.0

# 2. Separatriz Externa (Umbral desplazado A_c_ext)
# Representa un escenario de mayor Estrés Externo (E)
E_ext = 8  # Mayor presión externa
n_ext = 2  # Misma complejidad
A_c_ext = E_ext / n_ext  # Resultado: 4.0

# --- Rango de Valores A y Curvas ---
A_range = np.linspace(0, 6, 200)

# Curva principal (usando los parámetros internos)
R_values_int = resilience(A_range, E_int, n_int)

# --- Plot ---
plt.figure(figsize=(8,6))

# Curva Logística
plt.plot(A_range, R_values_int, color="blue", linewidth=2, label="Curva de Resiliencia $R(A, E, n)$")

# 1. Separatriz Interna (Umbral de Coherencia)
# El punto donde R=0.5 bajo las condiciones internas (E=6, n=2).
plt.axvline(x=A_c_int, linestyle="-", color="#32CD32", linewidth=2, label="Separatriz Interna ($A_{c}=3.0$)")

# 2. Separatriz Externa (Umbral de Estrés)
# El umbral al que se desplazaría el sistema bajo mayor presión (E=8, n=2).
plt.axvline(x=A_c_ext, linestyle="--", color="red", linewidth=2, label="Separatriz Externa ($A'_{c}=4.0$)")

# Línea de Resiliencia R=0.5
plt.axhline(y=0.5, linestyle=":", color="gray")

# Etiquetas de estado
plt.text(0.5, 0.2, "Estado Frágil", fontsize=10)
plt.text(4.5, 0.8, "Estado Resiliente", fontsize=10)
plt.text(3.1, 0.55, "Zona de Transición", fontsize=9, color='brown')

# Ejes y Título
plt.xlabel("Amplitud Adaptativa (A)")
plt.ylabel("Resiliencia R")
plt.title("TCRT: Curva Logística con Doble Separatriz (Formulación Base)")

plt.legend(loc='lower right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
