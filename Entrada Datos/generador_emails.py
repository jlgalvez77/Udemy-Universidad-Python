# Generador de Emails
nombre = input('Introduce el nombre: ')
apelllidos = input('Introduce los apellidos: ')
nombre_empresa = input('Introduce el nombre de la empresa: ')
extension_dominio = input('Introduce la extensión del diminio sin punto: ')

nombre_normalizado = nombre.replace(' ', ',').lower().strip()
apelllidos_normalizados = apelllidos.replace(' ', ',').lower().strip()
nombre_apellidos = '.'.join([nombre_normalizado, apelllidos_normalizados])

email = f'{nombre_apellidos}@{nombre_empresa}.{extension_dominio}'
print(email)