from data_ops import *


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
