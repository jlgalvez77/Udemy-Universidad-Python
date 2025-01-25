print('*** Sistema de reserva de Hotel ***')

COSTE_CON_VISTAS = 190.50
COSTE_SIN_VISTAS = 150.50

nombre_cliente = input('Introduce el nombre del cliente: ')
dias_estancia = int(input('¿Cuantos dias dura la estancia?: ' ))
vistas_mar = input('¿Tiene vistas al mar? (si/no) ').strip().lower()
vistas = vistas_mar == 'si'


print(f'Hola {nombre_cliente} ')
print(f'Tu habitacion {vistas_mar} tiene vistas al mar')
if vistas:
    print(f'El importe de la estancia es de {dias_estancia * COSTE_CON_VISTAS:.2f}€')
else:
    print(f'El importe de la estancia es de {dias_estancia * COSTE_SIN_VISTAS:.2f}€')