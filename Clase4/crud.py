from data import users

def crear_user(user):
    users.append(user)

def leer_user(user_id):
    return next((user for user in users if user['id'] == user_id), None)

def actualizar_user(user_id, updated_user):
    index = next((i for i, user in enumerate(users) if user['id'] == user_id), None)
    if index is not None:
        users[index] = {**users[index], **updated_user}

def borrar_user(users, user_id):
    return [user for user in users if user['id'] != user_id]


filter_users = lambda condition: [user for user in users if condition(user)]
