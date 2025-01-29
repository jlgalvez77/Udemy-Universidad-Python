# Función para saber si un número es par

# Definimos la función
def es_par(numero):
    if numero % 2 == 0:
        print('El número es par')
    else:
        print('El número es impar')

# Llamamos a la función
if __name__ == '__main__':
    numero = int(input('Introduce un número: '))
    es_par(numero)