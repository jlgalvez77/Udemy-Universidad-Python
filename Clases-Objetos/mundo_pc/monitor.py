class Monitor:
    contador_monitores = 0

    def __init__(self, marca, size):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.size = size

    def __str__(self):
        return (f'Id: {self.id_monitor}, Marca: {self.marca},'
                f'Tamaño: {self.size}')


if __name__ == '__main__':
    monitor1 = Monitor('HP', '35 Pulgadas')
    print(monitor1)
