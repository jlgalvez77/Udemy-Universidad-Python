# Factorial de un número
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
numero = int(input('Introduce un número para calcular su factorial: '))
print(factorial(numero))