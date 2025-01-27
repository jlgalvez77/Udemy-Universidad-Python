print('*** Manejo de Sets ***')

# Crear un conjunto, los elementos repetidos son ignorados
mi_set = {1, 2, 3, 4, 5, 4}
print(f'Mi ser: {mi_set}')

# Agregar elementos al set
mi_set.add(6)
mi_set.add(7)
print(f'Mi set modificado: {mi_set}')

# Eliminar un elemento del conjunto, al no segir un orden, no podemos borrar por indice, 
# directamente seleccionamos el valor a borrar
mi_set.remove(4)
print(f'Mi set modificado: {mi_set}')

# Iterar los elementos del set
for set in mi_set:
    print(f'Elemento del set: {set}')

# Comprobar si existe un elemento en ek set
print(6 in mi_set)

# Obtener la longitud del set
print(len(mi_set))