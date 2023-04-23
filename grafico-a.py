import matplotlib.pyplot as plt
import numpy as np

# Definindo as duas funções
def f1(x):
    return 1/x

def f2(x):
    return 1 + x**3

# Gerando um conjunto de pontos para x
x = np.linspace(-1, 1, 20)

# Plotando os gráficos
plt.plot(x, f1(x), label='y = 1/x')
plt.plot(x, f2(x), label='y = 1 + x^3')

# Adicionando as informações
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Exibindo o gráfico
plt.show()