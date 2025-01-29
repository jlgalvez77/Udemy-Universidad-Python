def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\nSuperpoder: {superpoder}')


# Llamar la función
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Sentido aracnido', 'Trepar paredes')

# Es opcional pasar argumentos variables
superheroe_superpoderes('Mi vecino', 'Juan Perez')