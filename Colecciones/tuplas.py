mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)

# Las tuplas no pueden ser modificadas, son inmutables

# Iteración de los elementos de la tupla
for elemento in mi_tupla:
    print(elemento, end=' ')


# Crear una tupla para una coordenada x, y
coordenadas = (3, 5)
# Acceder a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,

# Tupla anidada
tupla_anidada = (1, (2, 3), (4, 5))
print(f'Tupla anidada: {tupla_anidada}')