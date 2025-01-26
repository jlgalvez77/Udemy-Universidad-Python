print('*** Creación y validación de un password ***')

password_valido = False

while not password_valido:
    password = input('Crea una contraseña de al menos 6 caracteres: ')
    if len(password) >= 6:
        print('Contraseña aceptada')
        password_valido = True
    else:
        print('El password debe de tener al menos 6 caracteres\n')