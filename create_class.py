import bcrypt
import sqlite3
from datetime import datetime


class User:
    def __init__(self, first_name, last_name, email, password=None, city=None, state=None, phone_number=None, address=None, date_created=None, password_hash=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city
        self.state = state
        self.phone_number = phone_number
        self.address = address
        self.date_created = date_created or datetime.now()

        if password:
            self.set_password(password)
        elif password_hash:
            self.password = password_hash

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def update_email(self, new_email):
        self.email = new_email

    def save_to_db(self, cursor):
        cursor.execute("""
            INSERT INTO Users (first_name, last_name, email, password, city, state, phone_number, address, date_created)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.first_name, self.last_name, self.email, self.password, self.city, self.state, self.phone_number, self.address, self.date_created))
        cursor.connection.commit()

    @classmethod
    def load_from_db(cls, user_id, cursor):
        cursor.execute("SELECT * FROM Users WHERE user_id=?", (user_id,))
        row = cursor.fetchone()
        if row:
            return cls(row[1], row[2], row[3], password_hash=row[4], city=row[5], state=row[6], phone_number=row[7], address=row[8], date_created=row[9])  # Pass the password hash
        return None


connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password BLOB,
        city TEXT,
        state TEXT,
        phone_number TEXT,
        address TEXT,
        date_created TEXT
    )
""")

user = User(first_name="Enoka", last_name="Silipa", email="enoka.test@test.com", password="1234", phone_number="111-111-111", address="123 blvd")
user.save_to_db(cursor)

loaded_user = User.load_from_db(user_id=1, cursor=cursor)

if loaded_user:
    print(f"Name: {loaded_user.first_name} {loaded_user.last_name}")
    print(f"Email: {loaded_user.email}")

if loaded_user and loaded_user.check_password("1234"):
    print("Password matches!")
else:
    print("Password does not match!")

connection.close()
