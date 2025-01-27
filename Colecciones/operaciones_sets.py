print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unir dos sets, los une sin incluir los valores repetidos
union = a | b
print(f'Unión de a | b: {union}')

# Intersección, muestra los valores que hay en los dos conjuntos
interseccion = a & b
print(f'Intersección de a & b: {interseccion}')

# Diferencia, La operación de diferencia te dice qué elementos están en el primer 
# conjunto pero no están en el segundo.
diferencia = a - b
print(f'Diferencia a - b: {diferencia}')