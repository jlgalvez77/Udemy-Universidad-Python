print('*** Sentencia if-elif-else ***')

edad = int(input('Introduce tú edad: '))
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')
elif edad >= 13 and edad < 18:
    print(f'Eres un adolescente. Tienes {edad} años')
else:
    print(f'Eres menor de edad. Tienes {edad} años')