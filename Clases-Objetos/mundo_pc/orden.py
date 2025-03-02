class Orden:
    contador_ordenes = 0

    def __init__(self, computadores):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        # Recibimos la lista de objetos de tipo computadora
        self.computadores = computadores

    def agregar_computadora(self, computadora):
        self.computadores.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadores:
            computadoras_str += '\n' + computadora.__str__()
        return f'''Orden {self.id_orden}
        Computadoras: {computadoras_str}'''
