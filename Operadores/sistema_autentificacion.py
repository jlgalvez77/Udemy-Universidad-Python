USUARIO = 'admin'
PASSWORD = '123'

print('*** Sistema de Autentificación ***')
usuario = input('¿Cual es tu usuario?: ')
password = input('¿Cual es tu password?: ')

validacion = usuario == USUARIO and password == PASSWORD
print(f'¿Datos correctos? {validacion}')