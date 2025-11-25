# Función de umbral generalizado Ac(E, F, K; β, γ, ε, Λ)
def Ac_general(E, F, K, beta=1.0, gamma=0.8, eps=0.5, Lambda=3.0):
    rho = F / K
    denom = np.log(Lambda) - gamma * rho
    # Dominio de validez: denom > 0
    if denom <= 0:
        return np.nan
    return (beta * E) / denom - eps
