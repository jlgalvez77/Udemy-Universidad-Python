# Con el metodo split(), podemos extraer cadenas por separadores. Permite dividir una cadena en una lista de subcadenas basandose en un caracter separador,
# que por defecto es el espacio en blanco

datos = 'Hola Python'
lista = datos.split()
print(f'La lista es: {lista}')

datos = 'Jose,47,España'
lista = datos.split(',')
print(f'La lista es: {lista}')