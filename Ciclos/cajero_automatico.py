print('*** Aplicación de Cajero Automatico ***')

salir = False
saldo = 1000

while not salir:
    print('''
Operaciones que puedes realizar:
          1. Consultar Saldo
          2. Retirar Dinero
          3. Depositar Dinero
          4. Salir''')
    
    opcion = int(input('Escoje una opción: '))

    if opcion == 1:
        print(f'Tu saldo es {saldo}')
    if opcion == 2:
        retirada = int(input('Introduce la cantidad a retirar: '))
        if retirada > saldo:
            print(f'Fondos insuficientes, tu saldo es de {saldo}')
        else:
            saldo -= retirada
            print(f'Operaciòn realizada con exito')
    if opcion == 3:
        ingreso = int(input('Introduce la cantidad a ingresar: '))
        saldo += ingreso
        print(f'Operación realizada con exito')
    if opcion == 4:
        print('Saliendo del sistema...')
        salir = True