# Definimos la clase
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f'''Conduciendo el coche
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # Otra forma de definir el metodo get
    @property
    def marca(self):
        return self._marca

    # Modifica el valor del atributo
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Lee la  información del atributo
    @property
    def modelo(self):
        return self._modelo

    # Modifica el valor del atributo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    # Lee la  información del atributo
    @property
    def color(self):
        return self._color

    # Modifica el valor del atributo
    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creación del primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()

    # coche1.set_marca('Toyota 2')
    # coche1.set_modelo('Yaris 2')
    # coche1.set_color('Azul 2')
    # coche1.conducir()
    # Atributo de marca del coche1
    print(f'Atributo marca coche1: {coche1.marca}')
    coche1.marca = 'Toyota 2'
    print(f'Atributo marca coche1: {coche1.marca}')
