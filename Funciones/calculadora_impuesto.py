

def calcular_pago_total(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

pago_sin_impuesto = float(input('Proporciona el pago sin impuesto: '))
impuesto = float(input('Proporciona el valor del impuesto: '))
pago_con_impuesto = calcular_pago_total(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')