print('*** Cálculo Área y Perímetro de un Rectangulo ***')
base = float(input('Introduce la base del rectangulo: '))
altura = float(input('Introduce la altura del rectangulo: '))

area = base * altura
perimetro = 2 * (base + altura)

print(f'El área del rectángulo es: {area} y su perímetro es {perimetro}')