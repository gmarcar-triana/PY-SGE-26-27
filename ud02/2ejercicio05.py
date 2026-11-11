numeros = set()

cantidad_inicial = int(input('¿Cuántos números enteros quieres introducir al conjunto?: '))
for i in range(cantidad_inicial):
    num = int(input(f'Introduce el número {i + 1}: '))
    numeros.add(num)

print('Conjunto inicial:', numeros)

rep = True

while rep:
    print('1. Añadir el número 15')
    print('2. Eliminar el número 9')
    print('3. Calcular la cantidad de elementos')
    print('4. Comprobar si 6 está en el conjunto')
    print('0. Salir')
    opc = int(input('Elige una opción: '))

    match opc:
        case 1:
            numeros.add(15)
            print('Número 15 añadido. Conjunto actual:', numeros)

        case 2:
            if 9 in numeros:
                numeros.remove(9)
                print('Número 9 eliminado. Conjunto actual:', numeros)
            else:
                print('El número 9 no está en el conjunto.')

        case 3:
            print('Cantidad de elementos en el conjunto:', len(numeros))

        case 4:
            if 6 in numeros:
                print('El número 6 SÍ está en el conjunto.')
            else:
                print('El número 6 NO está en el conjunto.')

        case 0:
            print('Saliendo...')
            rep = False

        case _:
            print('Opción no válida.')
