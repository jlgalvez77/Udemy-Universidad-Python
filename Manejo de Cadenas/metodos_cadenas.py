cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')

mayusculas = cadena1.upper()
print(f'Mayúsculas: {mayusculas}')

minusculas = cadena1.lower()
print(f'Minúsculas: {minusculas}')

capitalizado = cadena1.capitalize()
print(f'Capitalizado: {capitalizado}')

titulo = cadena1.title()
print(f'Título: {titulo}')

reemplazo = cadena1.replace('Mundo', 'Python')
print(f'Reemplazo: {reemplazo}')

cadena2 = '    Espacios al inicio y al final    '
print(f'Cadena original: {cadena2}')
sin_espacios = cadena2.strip()
print(f'Sin espacios: {sin_espacios}')

# Largo de la cadena
largo = len(cadena1)
print(f'Largo de la cadena: {largo}')