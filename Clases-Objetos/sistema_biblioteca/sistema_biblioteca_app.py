from libro import Libro
from biblioteca import Biblioteca

print('*** Sistema de Bibliotecas ***')

# Creamos una instancia de una biblioteca
biblioteca1 = Biblioteca('Biblioteca')
print(f'Bienvenidos a a {biblioteca1.nombre}')

# Definimos libros
libro1 = Libro('El Señor de los Anillos','J.R.R. Tolkien', 'Fantasia')
libro2 = Libro('El Hobbit', 'J.R.R. Tolkien', 'Fantasia')
libro3 = Libro('Curso de Programación Java', 'Mariona Nadal', 'Manual')
libro4 = Libro('Las montañas de la locura', 'H.P. Lovecraft', 'Terror')

# Agregamos los libros a la biblioteca
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)
biblioteca1.agregar_libro(libro4)

# Libros por Genero
genero = 'Fantasia'
print(f'\nLibros de {genero}')
biblioteca1.buscar_libros_por_generos(genero)
# Libros por Autor
autor = 'J.R.R. Tolkien'
print(f'\nLibros de {autor}')
biblioteca1.buscar_libros_por_autor(autor)
# Mostrar todos los libros
biblioteca1.mostrar_todos_los_libros()