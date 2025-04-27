# Create Student class that takes name and marks of 3 subjects as arguments in constructor and calculate the average of marks obtained...

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def getavg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("The average score is",sum//3)

s1 = Student("Jalaj", [99,93,95])
print(s1.name)
s1.getavg()