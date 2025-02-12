# Definición de una classe(El nombre de la clase se inicia con mayusculas)
class Persona:

    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        
# Creación de objetos
if __name__ == '__main__':
    persona1 = Persona() # Se crea un objeto vacio en memoria
    persona1.inicializar_persona('Laila', 'Acosta')
    persona1.mostrar_persona()

    persona2 = Persona()
    persona2.inicializar_persona('Ian', 'Sanchez')
    persona2.mostrar_persona()