# Definición de una classe(El nombre de la clase se inicia con mayusculas)
class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la classe
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dirección de memoria de persona: {id(self)}')
        print(f'Dirección de memoria hexadecimal de persona: {hex(id(self))}')


# Creación de objetos
if __name__ == '__main__':
    # Creación del primer objeto
    persona1 = Persona('Laila', 'Acosta')
    persona1.mostrar_persona()

    # Creación del segundo objeto
    persona2 = Persona('Juan', 'Perez')
    persona2.mostrar_persona()
