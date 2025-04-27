#simple class and object example
class Student:
    name = "Karan"
    def __init__(self):      #default constructor....self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. 
        pass
    
    def __init__(self,name,marks):    #parameterized constructor
        self.name = name 
        self.marks = marks
        print("Adding name to database....")

s1 = Student("Karan",98)
print(s1.name)
print(s1.marks)

