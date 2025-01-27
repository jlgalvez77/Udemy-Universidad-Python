print('*** Calculo Promedio ***')

total_calificaciones = int(input('¿Cuantas notas quieres añadir? '))
calificaciones = []

# Iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'Calificación[{indice + 1}] = '))
    calificaciones.append(calificacion)

print(f'\nLas calificaciones son: {calificaciones}')

promedio = sum(calificaciones) / total_calificaciones

print(f'El promedio de las calificaciones es: {promedio:.2f}')