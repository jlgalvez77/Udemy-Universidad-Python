print('*** Sistema Envios ***')

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

destino = input('¿Cual es el destino del paquete? (Nacional/Internacional): ').strip().lower()
peso = float(input('¿Cual es el peso en kilogramos?: '))

if destino == 'nacional':
    print(f'El costo del envio es {peso * TARIFA_NACIONAL:.2f}')
elif destino == 'internacional':
    print(f'El costo del envio es {peso * TARIFA_INTERNACIONAL:.2f}')
else:
    print('Destino desconocido')