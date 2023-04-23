########### PROJETO COMPUTACIONAL 1 - MS211H ###########
# Guilherme Rafael Nunes de Oliveira - RA 221050
# Luis Filipe Ramos Afonso - RA 240486
# Pedro Marcelo Martelini - RA 187123

# Inputs
x0 = float(input('Chute Inicial: '))
e = float(input('Erro Tolerável: '))
N = int(input('Máximo de Iterações: '))

# Definição da função
def f(x):
    return (x**3)-5*x

# Definição da derivada da função
def g(x):
    return 3*(x**2)-5

# Método de Newton
def newton(x0, e, N):
    print('\nMÉTODO DE NEWTON')
    iter = 1
    converge = 1
    condicao = True
    while condicao:
        if g(x0) == 0.0:
            print('Erro: divisão por zero')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteração-%d, x1 = %0.6f, f(x1) = %0.6f e g(x1) = %0.6f' % (iter, x1, f(x1), g(x1)))
        x0 = x1
        iter = iter + 1

        if iter > N:
            converge = 0
            break

        condicao = abs(f(x1)) > e

    if converge == 1:
        print('\nA raiz encontrada é: %0.8f' % x1)
    else:
        print('\nA função não converge')

newton(x0, e, N)