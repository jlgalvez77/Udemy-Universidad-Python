# Imprimir del 1 al 5 de forma recursiva

# Definimos la función recursiva
def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end=' ')
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')


# Llamamos a la función
funcion_recursiva(5)