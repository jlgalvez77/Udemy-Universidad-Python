print('*** Calculadora con Funciones ***')

def mostrar_menu():
    print(f'''Operaciones que puedes realizar:
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir''')
    return int(input('Escoge una opción: '))

def pedir_valores():
    operando1 = float(input('Introduce el primer operando: '))
    operando2 = float(input('Introduce el segundo operando: '))
    return operando1, operando2

def ejecutar_operacion(operacion, salir):
    if opcion >= 1 and opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado}')
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'El resultado de la división es {resultado}')
    elif opcion == 5:
        print('Hasta pronto')
        salir = True
    else:
        print('Opción no valida')
    return salir

# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)