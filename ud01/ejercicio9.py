#9) Implementar un programa en Python que pida un número indeterminado de cadenas de caracteres 
# por el teclado, y cuando se finalice dicha introducción, muestre el listado de palabras.

palabras = []

while True:
    palabra = input("Introduce una palabra (o 'salir' para terminar): ")
    if palabra == "salir":
        break
    palabras.append(palabra)

print("Listado de palabras:")
for palabra in palabras:
    print(palabra)
    