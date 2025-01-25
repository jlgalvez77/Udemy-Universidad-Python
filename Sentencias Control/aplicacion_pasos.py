META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

nombre = input('Introduce tu nombre: ')
pasos_diarios = int(input('Introduce los pasos: '))

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO
meta_alcanzada = 'Si' if pasos_diarios >= META_PASOS_DIARIOS else 'No'

print(f'Hola {nombre}, hoy has quemado {calorias_quemadas} calorias y {meta_alcanzada} has alcanzado la meta de pasos diarias')