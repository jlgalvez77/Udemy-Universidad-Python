# **kwargs: Argumentos variables en forma de diccionario( key, value)

print('*** Argumentos variables en forma de diccionario ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la función
superheroe_superpoderes('Spiderman','Setido Aracnido','Trepamuros', Edad = 25, Compañia = 'Marvel')

# Los argumentos variables son opcionales
superheroe_superpoderes('Juan ')