print('*** Sitema de Descuentos ***')

importe = float(input('Cual fur el importe de tú compra? '))
miembro = input('¿Eres miembro de la tienda? (si/no)').lower()

if importe >= 100 and miembro == 'si':
    print('Obtienes un descuento del 10%')
    descuento = 0.1
    importe_del_descuento = importe * descuento
    importe_final = importe - importe_del_descuento
    print(f'Importe de la compra: {importe}€')
    print(f'Importe del descuento: {importe_del_descuento}€')
    print(f'Importe final de la compra con descuento: {importe_final}€')
elif miembro == 'si':
    print('Obtienes un descuento del 5%')
    descuento = 0.05
    importe_del_descuento = importe * descuento
    importe_final = importe - importe_del_descuento
    print(f'Importe de la compra: {importe}€')
    print(f'Importe del descuento: {importe_del_descuento}€')
    print(f'Importe final de la compra con descuento {importe_final}€')
else:
    print('No tienes descuentos')
    print(f'Importe de la compra {importe}€')