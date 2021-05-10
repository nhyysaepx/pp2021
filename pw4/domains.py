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

     def toString(self):
            print(f"""
                Name - {self.getName()}
                ID - {self.getID()}
                DoB - {self.getDoB()}
            """)