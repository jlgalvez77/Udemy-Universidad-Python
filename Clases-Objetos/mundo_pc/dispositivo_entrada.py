class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada

    def __str__(self):
        return f'Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}'
