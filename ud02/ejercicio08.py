tam = int(input('Tamaño de la lista: '))

lista = []

for i in range(tam):
    palabra = input('Ingrese una palabra: ')
    lista.append(palabra)

print(lista)

tam = int(input('Ingrese el tamaño de la lista a borrar: '))

listaBorrar = []

for i in range(tam):
    palabra = input('Ingrese una palabra: ')
    listaBorrar.append(palabra)

print(listaBorrar)

lista = [palabra for palabra in lista if palabra not in listaBorrar]

print(lista)