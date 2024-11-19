import sqlite3

def get_connection():
    """Функция для создания соединения с базой данных"""
    return sqlite3.connect("not_telegram.db")


def initiate_db():
    """Создание таблицы Products, если она не существует"""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )''')
    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"{username}", f"{email}", f"{age}", 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM Users WHERE username = ?", (username, ))
    result = cursor.fetchone()
    connection.close()
    if result == None:
        return False
    if result != None:
        return True


def get_all_products():
    """Получение всех товаров из таблицы Products"""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products

def upload_products():
    """Добавление нескольких товаров в таблицу Products"""
    products = [("Вариант 1", "простая палочка", 100),
                ("Вариант 2", "средняя палочка", 200),
                ("Вариант 3", "стандартная палочка", 300),
                ("Вариант 4", "сильная палочка", 400)
                ]
    connection = get_connection()
    cursor = connection.cursor()
    for prod in products:
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (prod[0], prod[1], prod[2]))
    connection.commit()
    connection.close()


