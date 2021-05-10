class Student:
    def __validateName(self, name):
        if(len(name) > 1):
            return true
        return False
    
    def __validateDoB(self, DoB):
        if(len(DoB) > 1):
            return True
        return False

    def _validateID(self, ID):
        if(len(ID) > 1):
            return True
        return False
    
    def __init(self, name, DoB, ID):

        if(self.__validateDoB(DoB) == False):
            print("Invalid DoB")
            return 
        
        if(self.__validateName(name) == False):
            print("Invalid Name")
            return 
        
        if(self.__validateID(ID) == False):
            print("Invalid ID")
            return 
        
        self.__name = name
        self.__DoB = DoB
        self.__ID = ID

    def getName(self):
        return self.__name
    
    def setName(self, name):
        if(self.__validateName(name)):
            self.__name = name
            return
        print("Invalid Name")

    def getID(self):
        return self.__ID
    
    def setID(self, ID):
        if(self.__validateID(ID)):
            self.__ID = ID
            return
        print("Invalid ID")
    
    def getDoB(self):
        return self.__DoB

    def setDoB(self, DoB):
        if(self.__DoB(DoB)):
            self.__DoB = DoB
            return
        print("Invalid DoB")
        
class Course:
    def __validateName(self, name):
        if(len(name) > 1):
            return True
        return False
    
    def __validateID(self, ID):
        if(len(ID) > 1):
            return True
        return False
    
    def __validateMark(self, Mark):
        if(len(Mark) > 1):
            return True
        
    def __init__(self, name, ID, Mark):
        if(self.__validateID(ID) == False):
            print("Invalid ID")
        return

        if(self.__validateMark(Mark) == False):
            print("Invalid Mark")
        return

        if(self.__validateName(name) == False):
            print("Invalid Name")
        return

        self.__name = name
        self.__ID = ID
        self.__Mark = {}

        def getName(self):
            return self.__name

        def setName(self, name):
            if(self.__validateName(name)):
                self.__name = name
                return
            print("Invalid Name")
        
        def getID(self):
            return self.__ID

        def setID(self, ID):
            if(self.__validateID(ID)):
                self.__ID = ID
                return
            print("Invalid ID")
        
        def setMark(self, students):
            for student in students:
                stdName = students.getName()
                mark = input("Enter the mark:")
                while (not(self.__validateMark(mark))):
                    print("Invalid Mark")
                    mark = input("Re-input the mark:")

def NumberofStudent():
    numberofstudent = int(input("- Enter the number of students in the class:"))
    return numberofstudent

def NumberofCourses():
    numberofcourses = int(input("- Enter the number of courses:"))
    return numberofcourses

def ShowCourse(courses):
    print("The courses that the students taking in are:")
    for course in courses:
        print(course.getName())


#main 
if __name__ == "main":
    students = []
    courses = []

    for i in range(NumberofStudent()):
        print('- Enter information of this student: ')
        name = input('- Enter student name: ')
        DoB = input('- Enter student dob: ')
        ID = input('- Enter ID of the student:')
        students.append(Student(name, DoB, ID))

    for i in range(NumberofCourses()):
        print('- Enter information of this course: ')
        name = input('- Enter course name: ')
        ID = input("- Enter ID of the student: ")
        Mark = input("- Enter the mark of the students: ")
        courses.append(Course(name, ID, Mark))