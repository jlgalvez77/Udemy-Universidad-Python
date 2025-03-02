from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden

print('*** Mundo PC ***')
# Computadora 1
teclado1 = Teclado('Razer', 'USB')
raton1 = Raton('Razer', 'Bluetooth')
monitor1 = Monitor('HP', '37')
computadora1 = Computadora('Intel', monitor1, teclado1, raton1)

# Computadora 2
teclado2 = Teclado('Razer', 'USB')
raton2 = Raton('Logitech', 'Bluetooth')
monitor2 = Monitor('AOC', '37')
computadora2 = Computadora('Alienware', monitor1, teclado1, raton1)

# Crear lista de computadoras
computadoras1 = [computadora1, computadora2]

orden1 = Orden(computadoras1)
print(orden1)