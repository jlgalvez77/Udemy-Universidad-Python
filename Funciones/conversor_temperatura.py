def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5/9

def celsius_to_farenheit(celsius):
    return celsius * 9/5 + 32

if __name__ == '__main__':
    while True:
        print('''
        Conversor de temperatura
            1 - Farenheit a Celsius
            2 - Celsius a Farenheit
            3 - Salir''')
        opcion = int(input('Selecciona una opción: '))

        if opcion == 1:
            farenheit = float(input('Proporciona los grados Farenheit: '))
            celsius = farenheit_to_celsius(farenheit)
            print(f'{farenheit} grados Farenheit son {celsius} grados Celsius')
        elif opcion == 2:
            celsius = float(input('Proporciona los grados Celsius: '))
            farenheit = celsius_to_farenheit(celsius)
            print(f'{celsius} grados Celsius son {farenheit} grados Farenheit')
        elif opcion == 3:
            break
        else:
            print('Opción incorrecta')