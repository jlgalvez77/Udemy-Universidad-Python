print('*** Verificar si un número es positivo')

numero = int(input('Introduce un número: '))

if numero > 0:
    print('Es positivo')
else:
    if numero < 0:
        print('Es negativo')
    else:
        print('Es cero')