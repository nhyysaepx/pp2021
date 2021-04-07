students = []
courses = []
course_mark = []

def numberofclassinput():
    print('How many students are there ?')
    number = int(input('- Number of student:'))
    return number

def StudentInfo():
    print('Enter the information about student')
    id = input('- id:')
    name = input('- name:')
    DoB = input('- DoB:')
    print(f"Student {name}, ID {id}, DoB {DoB}.")
    s = {"id": id, "name": name, "DoB": DoB}
    return s

def NumberofCourses():
    print('How many courses are there ?')
    numberofcourses = int(input('- Number of course:'))
    return numberofcourses

def CourseInfo():
    print('Enter the information about the course')
    id = input('- id:')
    coursename = input('- name:')
    print(f"Course {coursename}, ID {id}.")
    c = {"id": id, "course": coursename}
    return c 

def CourseMarkIntroduction():
    print('Enter the mark about the course')
    numberofstudent = int(input('- Number of student in the course:'))
    return numberofstudent

def CourseMarkInput():
    print('Enter the mark of each student')
    idcourse = input('- id:')
    namecourse = input('- name:')
    DoBcourse = input('- DoB:')
    markcourse = input('- Mark:')
    stdm = {"id": idcourse, "name": namecourse, "DoB": DoBcourse, "markcourse": markcourse}
    return stdm

def ViewStudent(students):
    print('Student Info:')
    print ("Name:" + s["name"])
    print ("ID:" + s["id"])
    print ("DoB:" + s["DoB"])

def ViewCourse(courses):
    print('Course Info:')
    for key in c:
        print(key, ':', c[key])

def ViewMark(course_mark):
    print('Mark Info:')
    for key in stdm:
        print(key, ':', stdm[key])


#main

print('-----------------------------------------')
print('Welcome to Student Mark Management System')
print('-----------------------------------------')

print("Let's start with entering the information about the student and the courses")

print("About Students:")

count = numberofclassinput()

for i in range (0, count):
    s = StudentInfo()
    students += s

print("About Courses:")


countcourse = NumberofCourses()

for n in range (0, countcourse):
    c = CourseInfo()
    courses += c

countstudentincourse = CourseMarkIntroduction()

for x in range (0, countstudentincourse):
    stdm = CourseMarkInput()
    course_mark += stdm


print('Choose the action you want to do')
print('1. View the information of the student')
print('2. View the information of the course')

action = int(input('- Action: '))

if action == 1:
    ViewStudent(students)

else:
    ViewCourse(courses)
    ViewMark(course_mark)

print('Want to do more?')
more = input('Y/N')

if more == 'Y':
    print('Choose the action you want to do')
    print('1. View the information of the student')
    print('2. View the information of the course')
    action2 = int(input('- Action: '))

    if action2 == 1:
        ViewStudent(students)

    else:
        ViewCourse(courses)
        ViewMark(course_mark)

else:
    print('Thank you for using me')



