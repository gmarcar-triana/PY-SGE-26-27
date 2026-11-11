tam = int(input('Tamaño de la lista: '))

lista = []

for i in range(int(tam)):
    palabra = input('Ingrese una palabra: ')
    lista.append(palabra)

print(lista)

nuevaPalabra = input('Ingrese una nueva palabra: ')
sustituir = input('Ingrese la palabra a sustituir: ')

for i in range(len(lista)):
    if lista[i] == sustituir:
        lista[i] = nuevaPalabra
        break

print(lista)