import domain
from input import *

def actions():
    print("""Choose the action:
    1 List students.
    2 List courses.
    3 Add course to study.
    4 Add student to course.
    5 Add student mark in the course.
    6 Get student GPA.
--------------------------------------------
    """)
    action = int(input())
    return action