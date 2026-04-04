import os
import subprocess
def clear_screen():
    subprocess.run("cls" if os.name=="nt" else "clear", shell=True)


def display_main_menu(active_student: int) -> None:
    clear_screen()
    print(f"Active Student ID: {active_student}")
    list = "L - List: lists all records in the course table"
    enroll = "E - Enroll: enrolls the active student in a course"
    withdraw = "W - Withdraw: removes a student from a course"
    search = "S - Search: Lists all matching courses"
    my_classes = "M - My Classes: Lists all Classes enrolled in by active student."
    exit_x = "X - Exit Application"

    main_menu_text = [list, enroll, withdraw, search, my_classes, exit_x]
    print(*main_menu_text, sep="\n")

    print(list)

def create_student() -> int:
    new_student_id = None
    #creation logic
    #return new id back to cakller
    pass

def run_query(query_type: int, student_id: int):
    pass


student_id: int = None
student_id = int(input("Enter Student ID: "))

if student_id < 0:
    student_id = create_student()
else:
    display_main_menu(student_id)

