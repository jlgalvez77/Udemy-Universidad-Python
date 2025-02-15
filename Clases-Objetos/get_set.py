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

    # Lee la  información del atributo
    def get_marca(self):
        return self._marca

    # Modifica el valor del atributo
    def set_marca(self, marca):
        self._marca = marca

    # Lee la  información del atributo
    def get_modelo(self):
        return self._modelo

    # Modifica el valor del atributo
    def set_modelo(self, modelo):
        self._modelo = modelo

    # Lee la  información del atributo
    def get_color(self):
        return self._color

    # Modifica el valor del atributo
    def set_color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creación del primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()

    coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()
