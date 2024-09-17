def agregar_producto_matriz(productos_matriz, producto):
    productos_matriz.append(producto)

def actualizar_producto_matriz(productos_matriz, id_producto, nuevos_datos):
    for i, producto in enumerate(productos_matriz):
        if producto[0] == id_producto:
            productos_matriz[i] = nuevos_datos
            return
    print(f"Producto con ID {id_producto} no encontrado.")

def eliminar_producto_matriz(productos_matriz, id_producto):
    productos_matriz[:] = [producto for producto in productos_matriz if producto[0] != id_producto]

def consultar_producto_matriz(productos_matriz, id_producto):
    for producto in productos_matriz:
        if producto[0] == id_producto:
            return producto
    print(f"Producto con ID {id_producto} no encontrado.")
    return None

