import domain
from input import *

def options():
    print("""What do yo want to do?:
    1 List students.
    2 List courses.
    3 Add student to the study group.
    4 Add course to study.
    5 Add student to course.
    6 Mark student in the course.
    7 Get student GPA.
--------------------------------------------
    """)
    option = int(input())
    return option