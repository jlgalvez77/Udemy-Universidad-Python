class Orden:
    contador_ordenes = 0

    def __init__(self, computadores):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
