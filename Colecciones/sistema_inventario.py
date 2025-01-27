print('*** Gestion de Inventario ***')

inventario = []

# Pedimos el número de productos que se van a introducir
numero_productos = int(input('¿Cuanto producto deseas agregar?: '))

# Pedimos los datos de los productos
for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    # Creamos el diccionario con los datos de los productos
    producto = {'id': indice + 1, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Añadimos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario inicial
print(f'\Inventario inicial: {inventario}')

# Buscar un producto por Id
id_buscar = int(input('\nIntroduce el ID del producto a buscar'))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'Información del producto encontrado: ')
    print(f'''Id: {producto_encontrado.get('id')}
    Nombre: {producto_encontrado.get('nombre')}
    Precio: {producto_encontrado.get('precio')}
    Cantidad: {producto_encontrado.get('cantidad')}
''')
else:
    print(f'Producto con id {id_buscar} NO encontrado')

# Mostrar el inventario detallado
print('\n--- Inventario detallado ---')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: {producto.get('precio')}
    Cantidad: {producto.get('cantidad')}
''')