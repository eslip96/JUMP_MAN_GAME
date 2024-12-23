import sqlite3


def create_schema(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS People (
        person_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        address_city TEXT,
        address_state TEXT,
        phone_number TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Birthdays (
        birthday_id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER,
        place_of_birth TEXT,
        year_of_birth INTEGER,
        month_of_birth INTEGER,
        FOREIGN KEY (person_id) REFERENCES People(person_id)
    );
    """)


def insert_person(cursor, first_name, last_name, address_city, address_state, phone_number):
    cursor.execute("""
    INSERT INTO People (first_name, last_name, address_city, address_state, phone_number)
    VALUES (?, ?, ?, ?, ?)
    """, (first_name, last_name, address_city, address_state, phone_number))


def insert_birthday(cursor, person_id, place_of_birth, year_of_birth, month_of_birth):
    cursor.execute("""
    INSERT INTO Birthdays (person_id, place_of_birth, year_of_birth, month_of_birth)
    VALUES (?, ?, ?, ?)
    """, (person_id, place_of_birth, year_of_birth, month_of_birth))


def create_database():
    connection = sqlite3.connect('friends_phonebook.db')
    cursor = connection.cursor()

    create_schema(cursor)

    people_data = [
        ("John", "Doe", "New York", "NY", "123-456-7890"),
        ("Jane", "Smith", "Los Angeles", "CA", "987-654-3210"),
        ("Alice", "Johnson", "Chicago", "IL", "555-123-4567"),
        ("Bob", "Lee", "Miami", "FL", "555-234-5678"),
        ("Charlie", "Brown", "Houston", "TX", "555-345-6789"),
        ("Diana", "Green", "Phoenix", "AZ", "555-456-7890"),
        ("Eva", "White", "Philadelphia", "PA", "555-567-8901"),
        ("Frank", "King", "San Francisco", "CA", "555-678-9012"),
        ("Grace", "Miller", "Dallas", "TX", "555-789-0123"),
        ("Hannah", "Scott", "Seattle", "WA", "555-890-1234"),
        ("Ian", "Adams", "Portland", "OR", "555-901-2345"),
        ("Jack", "Clark", "Atlanta", "GA", "555-012-3456"),
        ("Karen", "Rodriguez", "Boston", "MA", "555-123-4567"),
        ("Louis", "Martinez", "Denver", "CO", "555-234-5678"),
        ("Mona", "Wilson", "Austin", "TX", "555-345-6789")
    ]

    for person in people_data:
        insert_person(cursor, *person)

    birthdays_data = [
        (1, "New York", 1990, 5),
        (2, "Los Angeles", 1985, 8),
        (3, "Chicago", 1992, 11),
        (4, "Miami", 1988, 2),
        (5, "Houston", 1990, 7),
        (6, "Phoenix", 1987, 4),
        (7, "Philadelphia", 1993, 3),
        (8, "San Francisco", 1986, 12),
        (9, "Dallas", 1991, 1),
        (10, "Seattle", 1989, 6),
        (11, "Portland", 1994, 9),
        (12, "Atlanta", 1995, 10),
        (13, "Boston", 1986, 2),
        (14, "Denver", 1988, 5),
        (15, "Austin", 1990, 8)
    ]

    for birthday in birthdays_data:
        insert_birthday(cursor, *birthday)

    connection.commit()
    connection.close()
    print("DB'friends_phonebook.db' created!")


create_database()
