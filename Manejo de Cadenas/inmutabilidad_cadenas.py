cadena1 = 'Hola Mundo'
# cadena1[0] = 'h' -> Genera un error al ser las cadenas inmutables
cadena2 = cadena1
cadena1 = 'Adios' # Podemos hacer que la cadena apunte a otro objeto con otro valor
print(cadena1)
print(cadena2)