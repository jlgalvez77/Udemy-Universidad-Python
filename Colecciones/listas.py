# Listas

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceso a los elementos de una lista por su indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agregó el elemento 6')

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 34)
print(f'{mi_lista} -> Se agrego el elemento 34 en el indice 2')

# Reemplazar un elemento de la lista
mi_lista[5] = 99
print(f'{mi_lista} -> Se reemplazó el elemeto del indice 5')

# Eliminar elementos de una lista
# Usando el metodo remove
mi_lista.remove(4)
print(f'{mi_lista} -> Se eliminó el valor 4')
# Eliminar por indice usando el metodo pop
mi_lista.pop(1) # Elimina el elemento en el indice 1
print(f'{mi_lista} -> Se eliminó el índice 1') 
# Eliminar elementos con del
del mi_lista[2]
print(f'{mi_lista} -> Se eliminó el indice 2')

# Obtener sublistas
sublista = mi_lista[1:3] # Se genera una sublista del indice 1 al 2(El 3 no se incluye)
print(f'Sublista [1:3]-> {sublista}')