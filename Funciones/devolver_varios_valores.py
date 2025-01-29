def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función devuelve varios valore.')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('jose', 'galvez', 47)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')
