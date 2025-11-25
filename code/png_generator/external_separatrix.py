import matplotlib.pyplot as plt

# Valores críticos
Ac1 = 4.0
Ac2 = 4.5

# Crear figura
fig, ax = plt.subplots(figsize=(8, 3))

# Eje horizontal
ax.axhline(0, color='black')
ax.set_xlim(3, 6)
ax.set_ylim(0, 2)
ax.set_xlabel(r'$A$ (Threshold Axis)', fontsize=12)

# Líneas verticales
ax.axvline(Ac1, color='blue', linewidth=2)
ax.axvline(Ac2, color='green', linewidth=2)

# Zona sombreada
ax.fill_betweenx([0, 2], Ac1, Ac2, color='red', alpha=0.2)

# Etiquetas
ax.text(Ac1, 2.05, r'$A_c^{(1)}$', color='blue', ha='center')
ax.text(Ac2, 2.05, r'$A_c^{(2)}$', color='green', ha='center')
ax.text((Ac1 + Ac2)/2, 1, 'External Separatrix\n(Threshold Convergence)', color='darkred',
        ha='center', va='center', fontsize=10)

ax.text((Ac1 + Ac2)/2, 1.7, r'System ($A_c^{(1)}(E_1,n_1)$,\ $A_c^{(2)}(E_2,n_2)$)', color='black', ha='center')

# Estética
ax.set_yticks([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()
