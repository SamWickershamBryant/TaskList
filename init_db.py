import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tasks (title, content, duedate) VALUES (?, ?, ?)",
            ('First Task', 'Content for the first task', '2023-05-17')
            )

cur.execute("INSERT INTO tasks (title, content, duedate) VALUES (?, ?, ?)",
            ('Finish this project', 'learn flask and make web app', '2023-03-15')
            )

connection.commit()
connection.close()