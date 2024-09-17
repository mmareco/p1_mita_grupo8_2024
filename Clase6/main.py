# main.py

from crud_diccionario import agregar_producto, actualizar_producto, eliminar_producto, consultar_producto
from crud_matriz import agregar_producto_matriz, actualizar_producto_matriz, eliminar_producto_matriz, consultar_producto_matriz

# Definición de productos
productos = [
    {'id': 'P001', 'nombre': 'Televisor', 'precio': 30000, 'cantidad': 10},
    {'id': 'P002', 'nombre': 'Refrigerador', 'precio': 50000, 'cantidad': 5},
]

productos_matriz = [
    ['P001', 'Televisor', 30000, 10],
    ['P002', 'Refrigerador', 50000, 5],
]

# Ejemplos de uso para diccionarios
nuevo_producto = {'id': 'P003', 'nombre': 'Lavadora', 'precio': 25000, 'cantidad': 7}
agregar_producto(productos, nuevo_producto)
print("Productos después de agregar nuevo producto:", productos)

actualizar_producto(productos, 'P002', {'precio': 52000})
print("Productos después de actualizar producto P002:", productos)

eliminar_producto(productos, 'P001')
print("Productos después de eliminar producto P001:", productos)

producto = consultar_producto(productos, 'P002')
print("Consulta de producto P002:", producto)

# Ejemplos de uso para matrices
nuevo_producto_matriz = ['P003', 'Lavadora', 25000, 7]
agregar_producto_matriz(productos_matriz, nuevo_producto_matriz)
print("Productos matriz después de agregar nuevo producto:", productos_matriz)

actualizar_producto_matriz(productos_matriz, 'P002', ['P002', 'Refrigerador', 52000, 5])
print("Productos matriz después de actualizar producto P002:", productos_matriz)

eliminar_producto_matriz(productos_matriz, 'P001')
print("Productos matriz después de eliminar producto P001:", productos_matriz)

producto_matriz = consultar_producto_matriz(productos_matriz, 'P002')
print("Consulta de producto P002 en matriz:", producto_matriz)
