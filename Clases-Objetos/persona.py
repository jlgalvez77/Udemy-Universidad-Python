# Definición de una classe(El nombre de la clase se inicia con mayusculas)
class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        
# Creación de objetos
if __name__ == '__main__':
    persona1 = Persona('Latla', 'Acosta')
    persona1.mostrar_persona()

    persona2 = Persona('Juan', 'Perez')
    persona2.mostrar_persona()