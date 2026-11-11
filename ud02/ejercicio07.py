tam = int(input('Tamaño de la lista: '))

lista = []

for i in range(int(tam)):
    palabra = input('Ingrese una palabra: ')
    lista.append(palabra)

print(lista)

eliminar = input('Ingrese la palabra a eliminar: ')

for i in range(len(lista)):
    if lista[i] == eliminar:
        del lista[i]
        break

print(lista)