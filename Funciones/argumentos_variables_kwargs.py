print('*** Argumentos variables en forma de diccionario ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la función
superheroe_superpoderes('Spiderman','Setido','Trepamuros', Edad = 25, Compañia = 'Marvel')

# Los **kwargs son opcionales
superheroe_superpoderes('Juan ')