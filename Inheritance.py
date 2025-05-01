#When one class(child/derived) derives the properties and methods of another class(parent/base)

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod    #Decorator
    def stop():
        print("Car stop...")
    
class ToyotaCar(Car):   #Way of writing inheritance... ToyotaCar is child class and Car is parent class...
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
car1.start()

#Inheritance is of three types in python - Single, Multi-level and Multiple..

#The above example of Inheritance is Single Inheritance...

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car3 = Fortuner("Diesel")
car3.start()
print(car3.type)

#The above example is Multilevel Inheritance - parent -> child -> another child -> another child...

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#The above example is multiple inheritance i.e. two or more parent class and one derived class...

#Use of super keyword...It is used to access the properties of parent class...


class Car2:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod    #Decorator
    def stop():
        print("Car stop...")

class ToyataCar(Car2):
    def __init__(self,name,type):
        super().__init__(type)  #using super keyword to make access of the type property of parent class Car2...
        self.name = name

car3 = ToyataCar("Prius","Electric")
print(car3.type)
