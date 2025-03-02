
class Animal:
    def hacer_sonido(self):
        print('Hago sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Ladro')

class Gato(Animal):
    def hacer_sonido(self):
        print('Miago')

# Función polimorfica
def hacer_sonido_animal(animal):    # duck typing
    animal.hacer_sonido()

print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)
animal1.hacer_sonido()

print('\nClase Hija Perro: ')
perro1 = Perro()
perro1.hacer_sonido()
hacer_sonido_animal(perro1)

print('\nClase Hija Gato: ')
gato1 = Gato()
gato1.hacer_sonido()
hacer_sonido_animal(gato1)