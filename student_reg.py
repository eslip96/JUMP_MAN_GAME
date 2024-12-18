import sqlite3
from datetime import datetime


def create_schema(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS People (
        person_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        password TEXT NOT NULL,
        address TEXT,
        city TEXT,
        state TEXT,
        postal_code TEXT,
        active INTEGER DEFAULT 1
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        active INTEGER DEFAULT 1
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cohorts (
        cohort_id INTEGER PRIMARY KEY AUTOINCREMENT,
        instructor_id INTEGER,
        course_id INTEGER,
        start_date TEXT,
        end_date TEXT,
        active INTEGER DEFAULT 1,
        FOREIGN KEY (instructor_id) REFERENCES People(person_id),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student_Cohort_Registrations (
        student_id INTEGER,
        cohort_id INTEGER,
        registration_date TEXT,
        completion_date TEXT,
        drop_date TEXT,
        active INTEGER DEFAULT 1,
        PRIMARY KEY (student_id, cohort_id),
        FOREIGN KEY (student_id) REFERENCES People(person_id),
        FOREIGN KEY (cohort_id) REFERENCES Cohorts(cohort_id)
    );
    """)


def create_person(cursor, first_name, last_name, email, phone, password, address, city, state, postal_code):
    cursor.execute("""
    INSERT INTO People (first_name, last_name, email, phone, password, address, city, state, postal_code)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (first_name, last_name, email, phone, password, address, city, state, postal_code))


def create_course(cursor, name, description):
    cursor.execute("""
    INSERT INTO Courses (name, description)
    VALUES (?, ?)
    """, (name, description))


def create_cohort(cursor, instructor_id, course_id, start_date, end_date):
    cursor.execute("""
    INSERT INTO Cohorts (instructor_id, course_id, start_date, end_date)
    VALUES (?, ?, ?, ?)
    """, (instructor_id, course_id, start_date, end_date))


def assign_student_to_cohort(cursor, student_id, cohort_id):
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    INSERT INTO Student_Cohort_Registrations (student_id, cohort_id, registration_date)
    VALUES (?, ?, ?)
    """, (student_id, cohort_id, registration_date))


def remove_student_from_cohort(cursor, student_id, cohort_id):
    drop_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    UPDATE Student_Cohort_Registrations
    SET active = 0, drop_date = ?
    WHERE student_id = ? AND cohort_id = ?
    """, (drop_date, student_id, cohort_id))


def deactivate_course(cursor, course_id):
    cursor.execute("""
    UPDATE Courses
    SET active = 0
    WHERE course_id = ?
    """, (course_id,))


def deactivate_person(cursor, person_id):
    cursor.execute("""
    UPDATE People
    SET active = 0
    WHERE person_id = ?
    """, (person_id,))


def deactivate_cohort(cursor, cohort_id):
    cursor.execute("""
    UPDATE Cohorts
    SET active = 0
    WHERE cohort_id = ?
    """, (cohort_id,))


def complete_course_for_student(cursor, student_id, cohort_id):
    completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    UPDATE Student_Cohort_Registrations
    SET completion_date = ?
    WHERE student_id = ? AND cohort_id = ?
    """, (completion_date, student_id, cohort_id))


def reactivate_entity(cursor, table, entity_id):
    cursor.execute(f"""
    UPDATE {table}
    SET active = 1
    WHERE {table[:-1]}_id = ?
    """, (entity_id,))


def view_active_registrations(cursor, cohort_id):
    cursor.execute("""
    SELECT student_id, registration_date
    FROM Student_Cohort_Registrations
    WHERE cohort_id = ? AND active = 1
    """, (cohort_id,))
    return cursor.fetchall()


def view_active_cohorts(cursor, course_id):
    cursor.execute("""
    SELECT cohort_id, start_date, end_date
    FROM Cohorts
    WHERE course_id = ? AND active = 1
    """, (course_id,))
    return cursor.fetchall()


def view_active_people(cursor):
    cursor.execute("""
    SELECT person_id, first_name, last_name
    FROM People
    WHERE active = 1
    """)
    return cursor.fetchall()


def print_menu():
    print("""
    1. Create Person
    2. Create Course
    3. Create Cohort
    4. Assign Student to Cohort
    5. Remove Student from Cohort
    6. Deactivate Course
    7. Deactivate Person
    8. Deactivate Cohort
    9. Complete Course for Student
    10. Reactivate Entity (Course, Person, Cohort)
    11. View Active Registrations for Cohort
    12. View Active Cohorts for Course
    13. View All Active People
    14. Exit
    """)


def main():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    create_schema(cursor)

    while True:
        print_menu()
        choice = input("Enter your choice (1-14): ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            password = input("Password: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            postal_code = input("Postal Code: ")
            create_person(cursor, first_name, last_name, email, phone, password, address, city, state, postal_code)

        elif choice == '2':
            name = input("Course Name: ")
            description = input("Course Description: ")
            create_course(cursor, name, description)

        elif choice == '3':
            instructor_id = int(input("Instructor ID: "))
            course_id = int(input("Course ID: "))
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            create_cohort(cursor, instructor_id, course_id, start_date, end_date)

        elif choice == '4':
            student_id = int(input("Student ID: "))
            cohort_id = int(input("Cohort ID: "))
            assign_student_to_cohort(cursor, student_id, cohort_id)

        elif choice == '5':
            student_id = int(input("Student ID: "))
            cohort_id = int(input("Cohort ID: "))
            remove_student_from_cohort(cursor, student_id, cohort_id)

        elif choice == '6':
            course_id = int(input("Course ID: "))
            deactivate_course(cursor, course_id)

        elif choice == '7':
            person_id = int(input("Person ID: "))
            deactivate_person(cursor, person_id)

        elif choice == '8':
            cohort_id = int(input("Cohort ID: "))
            deactivate_cohort(cursor, cohort_id)

        elif choice == '9':
            student_id = int(input("Student ID: "))
            cohort_id = int(input("Cohort ID: "))
            complete_course_for_student(cursor, student_id, cohort_id)

        elif choice == '10':
            table = input("Entity Type (Courses, People, Cohorts): ").capitalize()
            entity_id = int(input(f"{table} ID: "))
            reactivate_entity(cursor, table, entity_id)

        elif choice == '11':
            cohort_id = int(input("Cohort ID: "))
            registrations = view_active_registrations(cursor, cohort_id)
            print("Active Registrations:", registrations)

        elif choice == '12':
            course_id = int(input("Course ID: "))
            cohorts = view_active_cohorts(cursor, course_id)
            print("Active Cohorts:", cohorts)

        elif choice == '13':
            people = view_active_people(cursor)
            print("Active People:", people)

        elif choice == '14':
            connection.commit()
            connection.close()
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
