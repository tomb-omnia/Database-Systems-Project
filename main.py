import os
import subprocess
import sqlite3

def initalize_database() -> None:
    connection = sqlite3.connect("school_database.db")
    cursor = connection.cursor()
    with open("create_database.sql", "r") as f:
        cursor.executescript(f.read())
    connection.commit()
    connection.close()
    print("Initalized database.")

def clear_screen():
    subprocess.run("cls" if os.name=="nt" else "clear", shell=True)

def student_exists(student_id:int ) -> bool:
    connection = sqlite3.connect("school_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM Student WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()
    connection.close()

    return result is not None

def display_main_menu(active_student: int) -> None:
    clear_screen()
    connection = sqlite3.connect("school_database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT Student.first_name, Student.last_name FROM Student WHERE student_id = ?", (active_student,))
    student_name = cursor.fetchone()
    connection.close()

    print(f"Active Student ID: {active_student}\nStudent Name: {student_name[0]} {student_name[1]}")
    main_menu: str = """    L - List: lists all records in the course table
    E - Enroll: enrolls the active student in a course
    W - Withdraw: removes a student from a course
    S - Search: Lists all matching courses
    M - My Classes: Lists all Classes enrolled in by active student.
    X - Exit Application"""
    print(main_menu)


def create_student() -> int:
    connection = sqlite3.connect("school_database.db")
    cursor = connection.cursor()

    first_name = None
    last_name = None

    while True:
        first_name = input("Enter Student's First Name: ")
        last_name = input("Enter Student's Last Name: ")
        print(f"Please confirm that you want to create a new Student ID for \"{first_name}\" \"{last_name}\"")
        confirmation = int(input("1 for Yes\nAny other number for No"))
        if confirmation == 1:
            break
        continue

    cursor.execute("INSERT INTO Student (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
    connection.commit()
    connection.close()

    new_student_id = cursor.lastrowid
    assert new_student_id is not None
    return new_student_id

def run_query(query_type: int, student_id: int):
    pass



student_id = -2

initalize_database()

while True:
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        clear_screen()
        print("Invalid Student ID.")
        print("Re-executing.")
        continue

    if student_id < -1:
        clear_screen()
        print("Invalid Student ID.")
        print("Re-executing.")
    elif student_exists(student_id=student_id):
        display_main_menu(active_student=student_id)
        break
    elif student_id == -1:
        student_id = create_student()
        display_main_menu(active_student=student_id)
        break
    else:
        clear_screen()
        print("The provided Student ID does NOT exists.")
        print("Re-executing.")




