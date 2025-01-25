print('*** Casa de los Espejos ***')

edad = int(input('¿Cuál es tu edad? '))
tienes_miedo_oscuridad = input('¿Tienes miedo a la oscuridad? (si/no) ').strip().lower()
tienes_miedo_oscuridad = tienes_miedo_oscuridad == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la casa de los espejos')
else:
    print('No puedes entrar')