snacks_disponibles = [
    {'id': 1,
     'nombre': 'Patatas',
     'precio': 30},
     {'id': 2,
      'nombre': 'Refresco',
      'precio': 50},
      {'id': 3,
       'nombre': 'Sandwich',
       'precio': 120}
]

# Creamos una lista vacia para almacenar los productos comprados
productos_comprados = []

def mostrar_snacks():
    print('--- Snacks disponibles ---')
    for snack in snacks_disponibles:
        print(f'Id: {snack.get('id')} -> {snack.get('nombre')} - {snack.get('precio')} $')

def buscar_snack_por_id(id_buscar):
    for snack in snacks_disponibles:
        if snack.get('id') == id_buscar:
            return snack
    # Si se llega al final de la lista y no se encontro el snack, retorna None
    return None

def comprar_snacks():
    id_snack = int(input('¿Qué snack quieres comprar (id)?'))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos_comprados.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_snack}')


def mostar_ticket():
    ticket = f'\t--- Ticket de Venta ---'
    total = 0
    for producto in productos_comprados:
        ticket += f'\n\t- {producto.get('nombre')} - {producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

def salir():
    print('Hasta pronto')
    
if __name__=='__main__':

    while(True):
        print('''
    Menú:
            1. Mostrar Snacks
            2. Comprar Snack
            3. Mostrar ticket
            4. Salir''')
        opcion = int(input('Escoge una opción: '))

        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostar_ticket()
        elif opcion == 4:
            print('Hasta pronto')
            break
        else:
            print('Opción no valida')