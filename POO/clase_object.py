class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # Sobreescribir el metodo __str__
    def __str__(self):
        return f'''Persona:
        nombre: {self._nombre}
        apellido: {self._apellido}
        Dirección de Memoria: {super.__str__(self)}'''

# Codigo Principal
persona1 = Persona('Ana', 'Marinez')
print(persona1) # El metodo __str__ se llama automaticamente desde print
# print(persona1.__str__()) Esto es opcional