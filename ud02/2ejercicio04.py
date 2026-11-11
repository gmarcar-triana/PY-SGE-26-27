inventario = {'manzanas': 10, 'naranjas': 5, 'peras': 8}

rep = True

while rep:
    print('1. Mostrar todas las claves y valores')
    print('2. Aumentar manzanas en 5')
    print('3. Eliminar peras')
    print('4. Calcular el total de frutas')
    print('0. Salir')
    opc = int(input('Elige una opción: '))

    match opc:
        case 1:
            print('\nInventario actual:')
            for fruta, cantidad in inventario.items():
                print(f'{fruta}: {cantidad}')

        case 2:
            if 'manzanas' in inventario:
                inventario['manzanas'] += 5
                print('Manzanas aumentadas. Nuevo total:', inventario['manzanas'])
            else:
                print('No hay manzanas en el inventario.')

        case 3:
            if 'peras' in inventario:
                del inventario['peras']
                print('Peras eliminadas del inventario.')
            else:
                print('Las peras ya no están en el inventario.')

        case 4:
            total = sum(inventario.values())
            print('Total de frutas en el frutero:', total)

        case 0:
            print('Saliendo...')
            rep = False

        case _:
            print('Opción no válida.')
