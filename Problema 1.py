import numpy as np
import matplotlib.pyplot as plt

# Datos de los días y consumos de energía
dias = np.array([1, 5, 9, 12])
consumos = np.array([20, 35, 60, 80])

# Estimación usando la interpolación de Newton
def diferencias_divididas(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    
    return coef[0,:]

def polinomio_newton(coef, x_data, x):
    n = len(x_data)
    polinomio = coef[0]
    for i in range(1, n):
        termino = coef[i]
        for j in range(i):
            termino *= (x - x_data[j])
        polinomio += termino
    return polinomio

# Coeficientes del polinomio de Newton
coef = diferencias_divididas(dias, consumos)

# Valores interpolados para el gráfico
x_vals = np.linspace(1, 12, 100)
y_vals = [polinomio_newton(coef, dias, x) for x in x_vals]

# Estimación en el día 7
x_estimar = 7
y_estimar = polinomio_newton(coef, dias, x_estimar)

# Graficar los puntos conocidos y el polinomio de Newton
plt.plot(x_vals, y_vals, label="Polinomio de Newton", color='blue')
plt.scatter(dias, consumos, color='red', label="Datos conocidos", zorder=5)
plt.scatter(x_estimar, y_estimar, color='green', label=f"Estimación en día {x_estimar}", zorder=5)

# Etiquetas y leyenda
plt.title("Interpolación por Newton del Consumo de Energía")
plt.xlabel("Día")
plt.ylabel("Consumo de Energía (kWh)")
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
