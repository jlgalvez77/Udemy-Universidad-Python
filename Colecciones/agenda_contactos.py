print('*** Agenda de Contactos ***')

# Creamos la agenda
agenda = {
    'Carlos': {
        'telefono': 567765456,
        'email': 'carlos@gmail.com',
        'direccion': 'Su calle, sin número'
    },
    'Maria': {
        'telefono': 675875456,
        'email': 'maria@gmail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': 123456789,
        'email': 'pedro@gmail.com',
        'direccion': 'Plaza Mayor 700'
    }
}

print(agenda)

# Acceder a la informacion de un contacto en especifico
print(f'''Información del contacto de Maria:
    Teléfono: {agenda["Maria"]['telefono']}
    Email: {agenda["Maria"]['email']}
    Dirección: {agenda["Maria"]['direccion']}
''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '564798213',
    'email': 'ana@gmail.com',
    'direccion': 'Calle Salvador Díaz 321'
}

# Eliminar un contacto existente
# agenda.pop('Pedro')
# del agenda['Pedro']
# print(agenda)

# Mostar todos los contactos de la agenda
print('\nContactos en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
''')