class Persona:
    # Atributo de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    # Metodo estatico
    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo estático')
        return Persona.contador_personas

    # Metodo de clase, forma recomendada por Python
    @classmethod
    def get_contador_personas_clase(cls):
        print('Metodo de clase')
        return cls.contador_personas


if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona ***')
    # Creamos el objeto de persona1
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    # Creamos el objeto de persona2
    persona2 = Persona('Juan', 'Perez')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')
