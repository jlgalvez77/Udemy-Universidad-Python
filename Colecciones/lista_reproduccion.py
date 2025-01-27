

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('¿Cuantas canciones quieres agregar?'))

# Iterar ca elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Introduce la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico - Metodo sort()
lista_reproduccion.sort()

# Mostrar la lista de canciones
print(f'\nLista de Reproducción en orden alfabético: ')
print(lista_reproduccion)

# Mostrar la lista iterando sus elementos
print('\nIteramos la playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')