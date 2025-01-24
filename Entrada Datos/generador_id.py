from random import randint

# Pedir los datos
nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
nacimiento = input('Introduce tú año de nacimiento(YYYY): ')

# Generar un número aleatorio de 4 cifras
numero_aleatorio = randint(1000, 9999)

nombre_normalizado = nombre[0:2].upper()
apellido_normalizado = apellido[0:2].upper()
nacimiento_normalizado = nacimiento[2:]

# Imprimimos el resultado
print('*** Generador de ID ***')
print(f'Tú nuevo ID es: {nombre_normalizado}{apellido_normalizado}{nacimiento_normalizado}{numero_aleatorio}')