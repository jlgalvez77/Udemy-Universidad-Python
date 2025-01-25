USER = 'admin'
PASSWORD = '1234'

print('*** Sistema de autentificación ***')
usuario = input('Introduce el nombre de usuario: ')
contrasena = input('Introduce la contraseña: ')

if usuario == USER and contrasena == PASSWORD:
    print('Bienvenido al sistema')
elif usuario != USER and contrasena == PASSWORD:
    print('Usuario invalido')
elif usuario == USER and contrasena != PASSWORD:
    print('Contraseña incorrecta')
elif usuario != USER and contrasena != PASSWORD:
    print('Usuario y contraseña invalidos')