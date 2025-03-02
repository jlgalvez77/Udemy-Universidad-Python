from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados

    def __str__(self):
        return f'Id: {self.id_teclado}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}'


if __name__ == '__main__':
    teclado1 = Teclado('Razer', 'Bluetooth')
    print(teclado1)
