nombre = input('Itroduce el nombre del empleado: ')
edad = int(input('Introduce la edad del empleado: '))
salario = float(input('Introduce el salario del empleado: '))
es_jefe = input('El empleado es jefe (s/n): ').lower()
if es_jefe == 's':
    es_jefe = True
else:
    es_jefe = False

print('*** Datos del empleado ***')
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Salario: {salario}')
print(f'Jefe: {es_jefe}')
print('Datos del empleado guardados correctamente')
