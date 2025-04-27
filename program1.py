#simple class and object example
class Student:

    college_name = "Abes Engineering College"   #Class attributes
    name = "Anonymous"

    def __init__(self):      #default constructor....self parameter is a mandatory argument and a reference to the current instance of the class, and is used to access variables that belongs to the class. 
        pass
    
    def __init__(self,name,marks):    #parameterized constructor
        self.name = name              #Instance attributes / Object Attributes
        self.marks = marks
        print("Adding name to database....")

s1 = Student("Karan",98)         #Creating Object
print(s1.name)                   #Output me Anonymous nhi aaega kyoki Class attributes priority >> Instance attributes priority
print(s1.marks)
print(s1.college_name)

#Output --
#Adding name to database....
#Karan
#98
#Abes Engineering College
