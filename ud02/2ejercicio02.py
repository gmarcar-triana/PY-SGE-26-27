productos = ('pan', 'leche', 'huevos', 'queso')
print(productos)

rep = True

while rep:
    print('1. Mostrar primer y último elemento')
    print('2. Contar cuántas veces aparece un producto')
    print('3. Modificar un producto')
    print('4. Añadir un producto')
    print('0. Salir')
    opc = int(input('Elige una opción: '))

    match opc:
        case 1:
            print('Primero: ', productos[0])
            print('Último: ', productos[-1])

        case 2:
            producto_buscar = input('Introduce el producto a buscar: ')
            cantidad = productos.count(producto_buscar)
            print(f'\n2. El producto "{producto_buscar}" aparece {cantidad} vez/veces.')
        case 3:
            print('\n3. Modificar un producto:')
            print('Productos actuales:', productos)
            indice = int(input('Introduce el índice del producto a modificar (0-3): '))
            if 0 <= indice < len(productos):
                nuevo_producto = input('Introduce el nuevo producto: ')
                lista_productos = list(productos)
                lista_productos[indice] = nuevo_producto
                productos = tuple(lista_productos)
                print('Tupla tras modificar un elemento:', productos)
            else:
                print('Índice fuera de rango.')
        
        case 4:
            print('\n4. Añadir un producto:')
            nuevo_producto = input('Introduce el nuevo producto: ')
            productos = productos + (nuevo_producto,)
            print('Tupla tras añadir un producto:', productos)
        
        case 0:
            print('Saliendo...')
            rep = False

        case _:
            print('Opción no válida.')
