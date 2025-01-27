print('*** Desempaqutado de Tuplas ***')

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Imprimimos los valores
print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')