def agregar_producto(productos, producto):
    productos.append(producto)

def actualizar_producto(productos, id_producto, nuevos_datos):
    for producto in productos:
        if producto['id'] == id_producto:
            producto.update(nuevos_datos)
            return
    print(f"Producto con ID {id_producto} no encontrado.")

def eliminar_producto(productos, id_producto):
    productos[:] = [producto for producto in productos if producto['id'] != id_producto]

def consultar_producto(productos, id_producto):
    for producto in productos:
        if producto['id'] == id_producto:
            return producto
    print(f"Producto con ID {id_producto} no encontrado.")
    return None

