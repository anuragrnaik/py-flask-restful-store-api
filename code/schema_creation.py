import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_items_table)

# cursor.execute("INSERT INTO items VALUES(null, 'test', 10.99)")

# user = (1, 'jhon', 'asdf')
# insert_query = "INSERT INTO users values (?, ?, ?)"
# cursor.execute(insert_query, user)

# users = [
#     (2, 'bob', 'xyz'),
#     (3, 'rolf', 'asdf')
# ]
# cursor.executemany(insert_query, users)


select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()