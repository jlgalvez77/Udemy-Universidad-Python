VALOR_MINIMO = 0
VALOR_MAXIMO = 5

valor_ingresado = int(input('Introduce un valor númerico: '))

dentro_rango = valor_ingresado >= VALOR_MINIMO and valor_ingresado <= VALOR_MAXIMO
print(f'Valor dentro de rango: {dentro_rango}')