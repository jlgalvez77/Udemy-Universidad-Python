nombre = 'Jose Galvez'
empresa = 'Futurmatica'
dominio = 'es'

nombreMinusculas = nombre.lower().strip()
empresaMinusculas = empresa.lower().strip()
dominioMinusculas = dominio.lower().strip()

nombre = nombreMinusculas.replace(' ', '.')

correo = f'Tu correo electronico es: {nombre}@{empresaMinusculas}.{dominioMinusculas}'
print(correo)
