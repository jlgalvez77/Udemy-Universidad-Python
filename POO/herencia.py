class Animal:
    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
    # Sobrescritura del metodo dormir, heredado de la clase Padre
    # Debe de tener el mismo nombre y los mismos parametros
    def dormir(self):
        print('Duermo 15 horas al dia')

# Programa  principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir() # Se llama al metodo de la clase hija, que sobreescribe el metodo de la clase padre
perro1.hacer_sonido()