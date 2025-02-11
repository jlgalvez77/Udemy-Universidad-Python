

def imprimir_persona(nombre, apellido = '', edad = 0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Llamamos la función pasando los argumentos de forma posicional
imprimir_persona('Jose', 'Galvez', 47)
# Llamar la función usando argumentos por nombre
imprimir_persona(nombre='Juan', apellido='Perez', edad=32)
# Llamar la función esando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=32, apellido='Perez', nombre='Juan')
# Argumentod con valor por default
imprimir_persona('Carlos')