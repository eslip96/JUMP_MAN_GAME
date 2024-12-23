import sqlite3


connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        make TEXT
    )
""")

cursor.executemany("""
    INSERT INTO Products (name, price, make) VALUES (?, ?, ?)
""", [
    ('DNA 15 Slim Messenger Bag (Graphite)', 159.95, 'Tenba'),
    ('DNA 15 Slim Messenger Bag (Cobalt)', 159.95, 'Tenba')
])

connection.commit()


def map_results(result_set, field_names_list):
    return [dict(zip(field_names_list, row)) for row in result_set]


connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

rows = cursor.execute("SELECT name, price FROM Products WHERE make='Tenba'").fetchall()
columns = ['name', 'price']

results = map_results(rows, columns)

print(f'{"price":<9} {"name":<25}')
for row in results:
    print(f'{row["price"]:<9} {row["name"]:<25}')
