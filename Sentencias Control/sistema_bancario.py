print('*** Bievebidos al Sistema Bancario ***')

salir_sistema_txt = input('¿Deseas salir del sistema? (si/no)').strip().lower()

salir_sistema = salir_sistema_txt == 'si'

if not salir_sistema:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')