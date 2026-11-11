claseA = {'Ana', 'Luis', 'Pedro'}
claseB = {'María', 'Luis', 'Sofía'}

rep = True

while rep:
    print('1. Mostrar los alumnos de ambas clases (unión)')
    print('2. Mostrar los alumnos comunes (intersección)')
    print('3. Mostrar alumnos solo de claseA')
    print('4. Añadir Carlos a claseB')
    print('0. Salir')
    opc = int(input('Elige una opción: '))

    match opc:
        case 1:
            union = claseA | claseB
            print('Alumnos de ambas clases:', union)

        case 2:
            interseccion = claseA & claseB
            print('Alumnos comunes:', interseccion)

        case 3:
            solo_a = claseA - claseB
            print('Alumnos solo en claseA:', solo_a)

        case 4:
            claseB.add('Carlos')
            print('Carlos añadido. Clase B actual:', claseB)

        case 0:
            print('Saliendo...')
            rep = False

        case _:
            print('Opción no válida.')
