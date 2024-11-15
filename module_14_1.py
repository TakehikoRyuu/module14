# Создание БД, добавление, выбор и удаление элементов.
import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARI KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    i = i+1
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

for i in range(10):
    if i % 2:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

cursor.execute("SELECT username FROM Users")
users = [row[0] for row in cursor.fetchall()]
users_to_del = users[::3]

for user in users_to_del:
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"{user}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(F'Имя: {user}')

connection.commit()
connection.close()
