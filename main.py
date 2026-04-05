from data_ops import *
import argparse

student_id = -2

parser = argparse.ArgumentParser(description="Montclair State University Student & Course Database\nBy Joseph Enigam")
parser.add_argument("--dev", action="store_true", help="Clears and rebuilds the database on each run")
args = parser.parse_args()

if args.dev:
    initalize_database()
else:
    print("Running in production mode, the database will not be reset on each successive execution of this python script.")

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
        break
    elif student_id == -1:
        student_id = create_student()
        break
    else:
        clear_screen()
        print("The provided Student ID does NOT exists.")
        print("Re-executing.")

while True:
    print("######\n")
    display_main_menu(active_student=student_id)
    parse_user_input(student_id)
