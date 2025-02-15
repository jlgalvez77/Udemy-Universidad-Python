class Aritmetica:
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

    def dividir(self):
        return self.operando1 / self.operando2

    def mostrar_resultado(self):
        print(f'El resultado de la suma es: {aritmetica1.sumar()}')
        print(f'El resultado de la resta es: {aritmetica1.restar()}')
        print(f'El resultado de la multiplicación es: {aritmetica2.multiplicar()}')
        print(f'El resultado de la división es: {aritmetica2.dividir()}')


if __name__ == '__main__':
    aritmetica1 = Aritmetica(5, 7)

    aritmetica2 = Aritmetica(12, 16)

    aritmetica1.mostrar_resultado()
