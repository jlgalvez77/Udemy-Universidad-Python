# Asignación multiple
x, y, z = 10, True, -16.5

print(f'El valor de x es: {x}, y: {y}, z: {z}')

# Asignación encadenada
a = b = c = 56
print(f'El valor de a es: {a}, b: {b}, c: {c}')

# Intercambio de valores de una variable sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x: {x}, y: {y}')
# Aplicamos el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f'Valores intercambiados, x: {x}, y: {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Introduce tu nombre y apellido, separados por comas.').split(',')
print(f'Tú nombre es: {nombre} y tu apellido: {apellido}.')