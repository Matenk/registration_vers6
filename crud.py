import sqlite3

# присвоение для db обращение к модулю .sqlite3 и вызов функции connect(создали/подключились к БД)
 # db - это объект класса sqlite3.Connection (представляет соединение с базой данных)
 # правило создания БД в python:
            # def initiate_db():
                # открыть базу
                # создать таблицу
                # сохранить изменения
                # закрыть базу

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
# cursor - это объект класса sqlite3.Cursor


# def initiate_db():
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Users(
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL UNIQUE,
#     password TEXT NOT NULL,
#     is_admin BOOLEAN NOT NULL DEFAULT FALSE
# );
# """)
#
#     connection.commit()
#     connection.close()
#
#
# initiate_db()


def create_user(username, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        print("Username already exists!")
        connection.close()
        return False



def login(username, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    check_user = cursor.execute(
        'SELECT * FROM Users WHERE username = ? AND password = ?',
        (username, password)
    ).fetchone()


    connection.close()

    return check_user


def get_user(id): # Возвращает конкретного юзера по ID для проверки в админке перед удалением
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    user = cursor.execute("SELECT * FROM Users WHERE id = ?", (id,)).fetchone()
    connection.close()
    return user


def read_users():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    connection.close()
    return users


def delete_user(id):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    check_id = cursor.execute("DELETE FROM Users WHERE id = ?", (id,)).fetchone()
    connection.commit()
    connection.close()
    return check_id
