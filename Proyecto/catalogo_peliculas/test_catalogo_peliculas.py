from Proyecto.catalogo_peliculas.dominio.Pelicula import Pelicula
from Proyecto.catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while True:
    try:
        print('''Opciones:
        1. Agregar película
        2. Listar películas
        3. Eliminar el archivo de películas
        4. Salir''')
        opcion = int(input('Selecciona una opción: '))

        if opcion == 1:
            nombre_pelicula = input('Introduce el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            print('Saliendo...')
            break
        else:
            print('Opción no reconocida')
    except Exception as e:
        print(f'Ocurrió un error {e}')
        opcion = None