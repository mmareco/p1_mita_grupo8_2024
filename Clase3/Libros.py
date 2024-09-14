def recortar_texto(texto, max_len):
    return texto[:max_len]

def formatear_texto(texto, formato):
    if formato == 'mayusculas':
        return texto.upper()
    elif formato == 'minusculas':
        return texto.lower()
    elif formato == 'capitalizado':
        return texto.capitalize()
    else:
        return texto

def mostrar_libros():
    print(f"{'ID':<5} {'TITULO':<30} {'AUTOR':<20} {'AÑO':<5}")
    print("=" * 60)
    for idx, libro in enumerate(libros):
        print(f"{idx:<5} {libro['titulo']:<30} {libro['autor']:<20} {libro['año']:<5}")
    print()

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = input("Ingrese el año de publicación: ")

    titulo = recortar_texto(titulo, 30)  #
    autor = formatear_texto(autor, 'mayusculas')  

    libros.append({"titulo": titulo, "autor": autor, "año": año})
    print("Libro agregado con éxito.\n")


def actualizar_libro():
    mostrar_libros()
    id_libro = int(input("Ingrese el ID del libro a actualizar: "))

    if 0 <= id_libro < len(libros):
        nuevo_titulo = input("Nuevo título (dejar en blanco para no cambiar): ")
        nuevo_autor = input("Nuevo autor (dejar en blanco para no cambiar): ")
        nuevo_año = input("Nuevo año (dejar en blanco para no cambiar): ")

        if nuevo_titulo:
            libros[id_libro]['titulo'] = recortar_texto(nuevo_titulo, 30)
        if nuevo_autor:
            libros[id_libro]['autor'] = formatear_texto(nuevo_autor, 'mayusculas')
        if nuevo_año:
            libros[id_libro]['año'] = nuevo_año

        print("Libro actualizado con éxito.\n")
    else:
        print("ID no válido.\n")

def eliminar_libro():
    mostrar_libros()
    id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    
    if 0 <= id_libro < len(libros):
        libros.pop(id_libro)
        print("Libro eliminado con éxito.\n")
    else:
        print("ID no válido.\n")

'''

def ordenar_libros():

'''

def mostrar_menu():
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Actualizar libro")
    print("4. Eliminar libro")
    print("5. Ordenar libros")
    print("6. Salir")

    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            mostrar_libros()
        elif opcion == '3':
            actualizar_libro()
        elif opcion == '4':
            eliminar_libro()
        #elif opcion == '5':
            #ordenar_libros()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.\n")


libros = []
mostrar_menu()


