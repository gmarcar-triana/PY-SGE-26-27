tam = int(input('Tamaño de la lista: '))

lista = []

for i in range(tam):
    palabra = input('Ingrese una palabra: ')
    lista.append(palabra)

print('Lista original:', lista)

listaReves = []

for i in range(tam - 1, -1, -1):
    listaReves.append(lista[i])

print(listaReves)
