# Factorial de un número
def factorial(numero):
    # Caso base, factorial 0! = 1 y 1! = 1
    if numero == 0 or numero == 1:
        return 1
    else:   # Caso recursivo, n! = n * (n-1)!
        return numero * factorial(numero - 1)
    
numero = int(input('Introduce un número para calcular su factorial: '))
print(f'El factorial de {numero} es: {factorial(numero)}')