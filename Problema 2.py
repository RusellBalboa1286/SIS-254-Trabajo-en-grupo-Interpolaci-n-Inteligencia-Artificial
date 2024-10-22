import numpy as np
import matplotlib.pyplot as plt

# Definir función de polinomio de Newton para evaluación en varios puntos
def evalua_polinomio(coef, x, x_vals):
    n = len(coef)
    p_vals = np.zeros_like(x_vals)
    for idx, val in enumerate(x_vals):
        p = coef[n-1]
        for k in range(1, n):
            p = coef[n-k-1] + (val - x[n-k-1]) * p
        p_vals[idx] = p
    return p_vals

# Datos originales
dias = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
consumo = np.array([150, 170, 200, 180, 220, 250, 230, 160, 180, 210])

# Coeficientes del polinomio calculados manualmente
coef = [150, 20, 10, -10, 7.08, -2.92, 0.78, -0.15, 0.03, -0.005]

# Valores de x y el rango extendido para incluir el jueves de la siguiente semana
x_vals = np.linspace(0, 10, 100)
y_polinomio = evalua_polinomio(coef, dias, x_vals)

# Plotear los datos
plt.figure(figsize=(10, 6))

# Graficar puntos originales
plt.scatter(dias, consumo, color='red', label='Datos originales (Consumo de agua)')
plt.plot(x_vals, y_polinomio, label='Interpolación de Newton', color='blue')

# Marcar el punto estimado para x = 10 (nuevo jueves)
p_estimada = evalua_polinomio(coef, dias, np.array([10]))[0]
plt.scatter([10], [p_estimada], color='green', label=f'Estimación Jueves (x=10): {p_estimada:.2f}')

# Configuraciones de la gráfica
plt.title("Interpolación de Newton para Consumo de Agua")
plt.xlabel("Día")
plt.ylabel("Consumo de agua (litros)")
plt.legend()
plt.grid(True)
plt.show()
