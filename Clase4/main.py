# main.py
from data import users
from crud import create_user, read_user, update_user, delete_user, filter_users

while True:
    print("\n1. Crear Usuario")
    print("2. Leer Usuario")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Filtrar Usuarios")
    print("6. Salir")

    opcion = input("Ingrese la opción: ")
    

    if opcion == '1':
        user_id = input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = {'id': user_id, 'name': nombre}
        if 'id' in usuario and 'name' in usuario:
            create_user(usuario)
        else:
            print("Datos del usuario inválidos.")

    elif opcion == '2':
        user_id = input("Ingrese el ID del usuario: ")
        usuario = read_user(user_id)
        if usuario:
            print(usuario)
        else:
            print("Usuario no encontrado.")

    elif opcion == '3':
        user_id = input("Ingrese el ID del usuario a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del usuario: ")
        usuario_actualizado = {'name': nombre}
        update_user(user_id, usuario_actualizado)

    elif opcion == '4':
        user_id = input("Ingrese el ID del usuario a eliminar: ")
        delete_user(user_id)

    elif opcion == '5':
        filtro_nombre = input("Ingrese el filtro de nombre: ")
        usuarios_filtrados = filter_users(lambda user: filtro_nombre.lower() in user['name'].lower())
        print(usuarios_filtrados)

    elif opcion == '6':
        break

    else:
        print("Opción inválida. Intente de nuevo.")
