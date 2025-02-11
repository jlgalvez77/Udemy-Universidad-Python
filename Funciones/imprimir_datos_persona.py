# Función que acepta argumentos variables en forma de llave-valor
def imprimir_datos_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Lamamos a la función
imprimir_datos_persona(nombre = 'Pedro', apellido = 'Perez', edad = 45, ciudad = 'Gijon')