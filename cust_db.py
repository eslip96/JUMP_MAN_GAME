import sqlite3

conn = sqlite3.connect("dp_customers.db")
cursor = conn.cursor()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        city TEXT,
        state TEXT,
        zipcode TEXT,
        phone TEXT,
        email TEXT
    );
    """)
    conn.commit()


create_table()


def view_all_customers():
    cursor.execute("SELECT customer_id, name, city, state, phone, email FROM customers")
    rows = cursor.fetchall()
    if rows:
        print("\n--- Customers ---")
        print("ID Name             City     State Phone      Email")
        for row in rows:
            print(f"{row[0]:<2} {row[1]:<16} {row[2]:<8} {row[3]:<5} {row[4]:<10} {row[5]}")
        customer_id = input("\nEnter Customer ID to View a Customer. Press 'Enter' to return to Main Menu: ")
        if customer_id:
            view_customer_detail(customer_id)
    else:
        print("\nNo customers found.")


def search_customers():
    search_term = input("Search Term: ")
    cursor.execute("SELECT customer_id, name, city, state, phone, email FROM customers WHERE name LIKE ?", (f"%{search_term}%",))
    rows = cursor.fetchall()
    if rows:
        print("\n--- Customers ---")
        print("ID Name             City     State Phone      Email")
        for row in rows:
            print(f"{row[0]:<2} {row[1]:<16} {row[2]:<8} {row[3]:<5} {row[4]:<10} {row[5]}")
    else:
        print("\nNo matching customers")
    input("Press 'Enter' to return to Main Menu")


def view_customer_detail(customer_id):
    cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
    customer = cursor.fetchone()
    if customer:
        print("\n*** Customer Details ***")
        print(f"ID:      {customer[0]}")
        print(f"Name:    {customer[1]}")
        print(f"Address: {customer[2]}")
        print(f"City:    {customer[3]}")
        print(f"State:   {customer[4]}")
        print(f"Zipcode: {customer[5]}")
        print(f"Phone:   {customer[6]}")
        print(f"Email:   {customer[7]}")

        action = input("\nTo update a field, enter the first letter of the field.\nTo delete this record, type 'DELETE'.\nTo return to the main menu, press 'Enter'.\n")
        if action.lower() == 'd':
            delete_customer(customer_id)
        elif action.lower() in ['n', 'a', 'c', 's', 'z', 'p', 'e']:
            update_customer_field(customer_id, action.lower())
    else:
        print("\nCustomer not found.")


def add_new_customer():
    print("\n### New Customer ###")
    name = input("Name    : ")
    address = input("Address : ")
    city = input("City    : ")
    state = input("State   : ")
    zipcode = input("Zipcode : ")
    phone = input("Phone   : ")
    email = input("Email   : ")

    cursor.execute(
        "INSERT INTO customers (name, address, city, state, zipcode, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, address, city, state, zipcode, phone, email),
    )
    conn.commit()
    print(f"\nCustomer \"{name}\" added!")


def update_customer_field(customer_id, field):
    field_map = {
        'n': "name",
        'a': "address",
        'c': "city",
        's': "state",
        'z': "zipcode",
        'p': "phone",
        'e': "email"
    }
    field_name = field_map[field]
    current_value = cursor.execute(f"SELECT {field_name} FROM customers WHERE customer_id = ?", (customer_id,)).fetchone()[0]
    new_value = input(f"Current {field_name.capitalize()}: {current_value}\nNew {field_name.capitalize()}: ")

    cursor.execute(f"UPDATE customers SET {field_name} = ? WHERE customer_id = ?", (new_value, customer_id))
    conn.commit()
    print(f"\nSUCCESS: {field_name.capitalize()} updated!")


def delete_customer(customer_id):
    cursor.execute("SELECT name FROM customers WHERE customer_id = ?", (customer_id,))
    customer = cursor.fetchone()
    if customer:
        customer_name = customer[0]
        confirm = input(f"Are you SURE you want to DELETE Customer {customer_id}: \"{customer_name}\"? (Y/N): ")
        if confirm.lower() == 'y':
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
            conn.commit()
            print(f"\nCustomer \"{customer_name}\" has been deleted!")
        else:
            print("\nDeletion canceled.")
    else:
        print(f"\nNo customer found with ID: {customer_id}.")


def main():
    while True:
        print("\n**** Customer Database ****")
        print("\n[1] View All Customers")
        print("[2] Search Customers")
        print("[3] Add a New Customer")
        print("[4] Delete a Customer")
        print("[Q] Quit")

        choice = input("\n>>> ").lower()
        if choice == '1':
            view_all_customers()
        elif choice == '2':
            search_customers()
        elif choice == '3':
            add_new_customer()
        elif choice == '4':
            customer_id = input("\nEnter the Customer ID to delete: ")
            if customer_id.isdigit():
                delete_customer(customer_id)
            else:
                print("\nInvalid input. Please enter a valid Customer ID.")
        elif choice == 'q':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
    conn.close()
