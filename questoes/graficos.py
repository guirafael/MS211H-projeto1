import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import math

pi = math.radians(180)

# Define a função f(x)
def f(x):
    return (x**3)-2*x+2

# Define a função derivada
def df(x):
    return 3*(x**2)-2

# Define o chute inicial, a tolerância e o número máximo de iterações
x0 = 5
epsilon = 9e-7
max_iter = 100

# Cria listas vazias para armazenar os valores das iterações
x_values = []
f_values = []

# Aplica o método de Newton
for i in range(max_iter):
    f_val = f(x0)
    df_val = df(x0)
    x1 = x0 - f_val / df_val
    x_values.append(x1)
    f_values.append(f_val)
    if abs(f_val) < epsilon:
        break
    x0 = x1

# Mostra a solução com 6 casas decimais
print("Solução: {:.6f}".format(x1))

# Plota o gráfico de f(x)
x = np.linspace(0.1, 2, 1000)
y = f(x)
plt.plot(x, y, label='f(x)')

# Plota o gráfico da linha y=0
plt.plot(x, np.zeros(len(x)), 'k--')

# Plota um ponto na solução encontrada
plt.plot(x1, 0, 'ro')

# Configura o gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Mostra o gráfico
plt.show()

# Mostra a tabela com os valores das iterações
table = []
for i in range(len(x_values)):
    table.append([i+1, x_values[i], f_values[i]])
print(tabulate(table, headers=['Iteração', 'x', 'f(x)']))