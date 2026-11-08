#3) Mostrar el precio final (con IVA) de un producto con un valor de 100 euros, suponiendo que el IVA es el 21%.

precio = 100
iva = 21

precioConIva = precio + (precio * iva / 100)

print('El precio', precio, 'con IVA es', precioConIva, '€')
