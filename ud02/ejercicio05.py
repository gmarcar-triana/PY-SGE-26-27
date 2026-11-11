#5. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga
#cuántas veces aparece esa palabra en la lista.

tam = int(input('Elige tamaño lista'))

lista = []

for i in range(tam):
    lista.append(input('Introduce palabra para añadir: '))

buscar = input('Introduce palabra a buscar: ')

for i in lista:
    if i == buscar:
        print(f'Aparece {lista.count(buscar)} veces')
        break
