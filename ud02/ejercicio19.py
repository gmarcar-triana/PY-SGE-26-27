precios = [10, 25, 15, 30, 50]

ventas = [
    [10, 5, 2, 8, 3],
    [4, 12, 7, 6, 2],
    [15, 8, 10, 4, 5],
    [6, 9, 3, 7, 4]
]

rep = True
totales_articulos = []
cantidad_sucursal_2 = 0
cantidad_articulo_3_sucursal_1 = 0
recaudacion_sucursales = []
recaudacion_total = 0
sucursal_mayor = 0

while rep:
    print("\n--- MENÚ ---")
    print("1. Cantidades totales de cada artículo")
    print("2. Cantidad de artículos en la sucursal 2")
    print("3. Cantidad del artículo 3 en la sucursal 1")
    print("4. Recaudación total de cada sucursal")
    print("5. Recaudación total de la empresa")
    print("6. Sucursal de mayor recaudación")
    print("7. Salir")
    
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            totales_articulos = [sum(art) for art in zip(*ventas)]
            print("Cantidades totales de cada artículo:", totales_articulos)
       
        case "2":
            cantidad_sucursal_2 = sum(ventas[1])
            print("Cantidad de artículos en la sucursal 2:", cantidad_sucursal_2)
       
        case "3":
            cantidad_articulo_3_sucursal_1 = ventas[0][2]
            print("Cantidad del artículo 3 en la sucursal 1:", cantidad_articulo_3_sucursal_1)
       
        case "4":
            recaudacion_sucursales = [sum(q * p for q, p in zip(sucursal, precios)) for sucursal in ventas]
            print("Recaudación total de cada sucursal:", recaudacion_sucursales)
       
        case "5":
            recaudacion_sucursales = [sum(q * p for q, p in zip(sucursal, precios)) for sucursal in ventas]
            recaudacion_total = sum(recaudacion_sucursales)
            print("Recaudación total de la empresa:", recaudacion_total)
      
        case "6":
            recaudacion_sucursales = [sum(q * p for q, p in zip(sucursal, precios)) for sucursal in ventas]
            sucursal_mayor = recaudacion_sucursales.index(max(recaudacion_sucursales)) + 1
            print("Sucursal de mayor recaudación:", sucursal_mayor)

        case "7":
            rep = False

        case _:
            print("Opción no válida")