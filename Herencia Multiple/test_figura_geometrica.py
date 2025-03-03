from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5, 'Rojo')
print(f'Cálculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(6, 9, 'Verde')
print(f'Cálculo area rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)