print('*** Sistema de Gestión de Inventario ***')

continuar = False

inventario = [
    {'Id': 1,
     'Nombre': 'Pantalones',
     'Precio': 59.99,
     'Cantidad': 25},
     {
         'Id': 2,
         'Nombre': 'Camisa',
         'Precio': 29.99,
         'Cantidad': 20
     },
     {
         'Id': 3,
         'Nombre': 'Zapatos',
         'Precio': 40,
         'Cantidad': 15

     }
]

def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('Id')}, Nombre: {producto.get('Nombre')}, Precio: {producto.get('Precio')}, Cantidad: {producto.get('Cantidad')}')

def agregar_producto():
    print('--- Agregar Nuevo Producto ---')
    Id = int(input('Id: '))
    Nombre = input('Nombre: ')
    Precio = float(input('Precio: '))
    Cantidad = int(input('Precio: '))
    nuevo_producto = {'Id': Id, 'Nombre': Nombre, 'Precio': Precio, 'Cantidad': Cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')

def buscar_id():
    print('--- Buscar por Id ---')
    id_buscar = int(input('Ingresa el Id a buscar'))
    for producto in inventario:
        if producto.get('Id') == id_buscar:
            print('\nInformación del producto encontrado')
            print(f'Id: {producto.get('Id')}, Nombre: {producto.get('Nombre')}, Precio: {producto.get('Precio')}, Cantidad: {producto.get('Cantidad')}')
            return
    print('Producto no encontrado')

# Programa principal
if __name__ == '__main__':
    while True:
        print('''--- Menú ---
            1. Mostrar inventario
            2. Agregar nuevo producto
            3. Buscar por Id
            4. Salir''')
        opcion = int(input('Introduce un opción (1-4): '))

        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_id()
        elif opcion == 4:
            print('Hasta pronto')
            break
        else:
            print('Opción no valida')

