# Programa para administrar una lista de suscriptores utilizando su email.
# A medida que la lista crece, hay que asegurarse de que no tenga suscriptores duplicados.
# Tambien se pueden agregar y eliminar suscriptores

print('*** Lista de Suscrptores ***')

# Definimos el set inicial
suscriptores = set()

numero_suscriptores = int(input('¿Cuantos suscriptores quieres añadir?: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Introduce el email del nuevo suscriptor'))

print(f'Lista de suscriptores inicial: {suscriptores}')

# Verificar si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Introduce el email para añadir a la lista de suscripción: ')
if nuevo_suscriptor in suscriptores:
    print('El nuevo suscriptor ya está en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print('El nuevo suscriptor ha sido añadido a la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminar un suscriptor
eliminar_suscriptor = input('Introduce el email del suscriptor para eliminarlo de la lista: ')
suscriptores.remove(eliminar_suscriptor)
print(f'El suscriptor {eliminar_suscriptor} ha sido eliminado de la lista')

# Verificar la cantidad total de suscriptores
print(f'La cantidad total de suscriptores es: {len(suscriptores)}')

# Mostrar todos los suscriptores
print('--- Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(suscriptor)