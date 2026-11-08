#4. Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un
#número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir
#la lista.

print('ejercicio4')

rep = 0
lista = []

while rep == 0:
    print('1. Mostar lista')
    print('2. Añadir a la lista')
    print('0. Salir')
    opc = input('Elige una opcion')

    match opc:
        case '1':
            print(lista)

        case '2':
            lista.append(input('Introduce palabra para añadir: '))
            print('Palabra añadida')

        case '0':
            rep = 1
            print('Saliendo...')

        case _:
            print('Opción no válida')