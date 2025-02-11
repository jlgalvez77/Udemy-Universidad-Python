# Función sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for valor in  args:
        total += valor
    return total

# Llamamos a la función sumar
resultado = sumar(1, 2, 3, 4, 5)
print(f'El resultado de la suma es: {resultado}')