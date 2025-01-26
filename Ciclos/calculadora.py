print('*** Calculadora en Python ***')


salir = False

while not salir:
    print('''
Operaciones que puedes realizar:
      1. Suma
      2. Resta
      3. Multiplicación
      4. División
      5. Salir''')
    opcion = int(input('Selecciona una operación a realizar: '))

    if opcion == 1:
        operando1 = float(input('Introduce el primer operando: '))
        operando2 = float(input('Introduce el segundo operando: '))
        suma = operando1 + operando2
        print(f'La suma de {operando1} y {operando2} es: {suma}')
    if opcion == 2:
        operando1 = float(input('Introduce el primer operando: '))
        operando2 = float(input('Introduce el segundo operando: '))
        resta = operando1 - operando2
        print(f'La resta de {operando1} menos {operando2} es: {resta}')
    if opcion == 3:
        operando1 = float(input('Introduce el primer operando: '))
        operando2 = float(input('Introduce el segundo operando: '))
        multiplicacion = operando1 * operando2
        print(f'La miltiplicación de {operando1} por {operando2} es: {multiplicacion}')
    if opcion == 4:
        operando1 = float(input('Introduce el primer operando: '))
        operando2 = float(input('Introduce el segundo operando: '))
        division = operando1 / operando2
        print(f'La división de {operando1} entre {operando2} es: {division}')
    if opcion == 5:
        print('Saliendo de la calculadora')
        salir = True