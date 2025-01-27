# Combinar Listas y Tuplas

# Definimos una lista que almacena tuplas
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

print('*** Unpacking ***')
# Unpacking
for producto in productos:
    id, descripcion, precio = producto
    print(f'Producto: Id = {id}, descripción = {descripcion} , precio = {precio}')

total = 0
# Imprimir la información de cada producto y calcular el precio total
print('*** Productos ***')
for producto in productos:
    print(f'ID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}')
    total += producto[2]

print(f'El precio total de los productos es: {total}')

