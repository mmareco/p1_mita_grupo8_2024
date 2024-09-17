from validaciones import validar_datos

base_datos = []

def agregar_dato(datos):
    valido, mensajes = validar_datos(datos)
    if valido:
        base_datos.append(datos)
        print("Datos agregados correctamente.")
    else:
        for mensaje in mensajes:
            print(mensaje)

def mostrar_datos():
    if base_datos:
        for idx, dato in enumerate(base_datos):
            print(f"Registro {idx + 1}: {dato}")
    else:
        print("No hay datos disponibles.")

def actualizar_dato(indice, datos_nuevos):
    if 0 <= indice < len(base_datos):
        valido, mensajes = validar_datos(datos_nuevos)
        if valido:
            base_datos[indice] = datos_nuevos
            print("Datos actualizados correctamente.")
        else:
            for mensaje in mensajes:
                print(mensaje)
    else:
        print("Índice de registro inválido.")

def eliminar_dato(indice):
    if 0 <= indice < len(base_datos):
        base_datos.pop(indice)
        print("Datos eliminados correctamente.")
    else:
        print("Índice de registro inválido.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar dato")
        print("2. Mostrar datos")
        print("3. Actualizar dato")
        print("4. Eliminar dato")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            correo = input("Ingresa el correo electrónico: ")
            telefono = input("Ingresa el número de teléfono: ")
            codigo_postal = input("Ingresa el código postal: ")
            fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
            datos = {'correo': correo, 'telefono': telefono, 'codigo_postal': codigo_postal, 'fecha': fecha}
            agregar_dato(datos)
        
        elif opcion == '2':
            mostrar_datos()
        
        elif opcion == '3':
            mostrar_datos()
            indice = int(input("Ingresa el número del registro a actualizar: ")) - 1
            correo = input("Ingresa el nuevo correo electrónico: ")
            telefono = input("Ingresa el nuevo número de teléfono: ")
            codigo_postal = input("Ingresa el nuevo código postal: ")
            fecha = input("Ingresa la nueva fecha (YYYY-MM-DD): ")
            datos_nuevos = {'correo': correo, 'telefono': telefono, 'codigo_postal': codigo_postal, 'fecha': fecha}
            actualizar_dato(indice, datos_nuevos)
        
        elif opcion == '4':
            mostrar_datos()
            indice = int(input("Ingresa el número del registro a eliminar: ")) - 1
            eliminar_dato(indice)
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Inténtalo de nuevo.")
