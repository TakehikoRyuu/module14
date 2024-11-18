# Создание БД, добавление, выбор и удаление элементов.
import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    i = i + 1
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}", ))
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

for i in range(10):
    if i % 2:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

cursor.execute("SELECT username FROM Users")
users = [row[0] for row in cursor.fetchall()]
users_to_del = users[::3]

for user in users_to_del:
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"{user}",))

cursor.execute("DELETE FROM Users WHERE username = ?", (f"User6", ))

cursor.execute("SELECT id, username, email, age, balance FROM Users")
users = cursor.fetchall()
for user in users:
    print(F'Имя: {user}')

cursor.execute("SELECT SUM(balance) FROM Users")
totat1 = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
totat2 = cursor.fetchone()[0]
result = totat1/totat2
print(result)

connection.commit()
connection.close()

# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))
#
# cursor.execute("DELETE FROM Users WHERE username = ?", ('newuser{i}', ))
#
# cursor.execute("DELETE FROM Users WHERE username = ?", (f'newuser{i}', ))