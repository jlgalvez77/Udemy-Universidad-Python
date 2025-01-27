print('*** Comprensión de listas ***')

# Unalista con el cuadrado de cada número
numeros =[1, 2, 3, 4, 5, 6]

cuadrados = [x**2 for x in numeros]
print(cuadrados)


# Lista de números pares
numeros = range(100 + 1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)


# Lista saludando a cada nombre
nombres = ['Pepe', 'Juan', 'Jose','Pedro']
saludos = [f'Hola {nombre}' for nombre in nombres]
print(saludos)