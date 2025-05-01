# Static methods - Methods that don't use the self parameter (work at class level)

class Student:

    @staticmethod #A decorator
    def college():
        print("ABC College")

#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

s1 = Student()
s1.college()

#Concept of Private attributes and Private methods by adding two "__" underscores in front of them...

class Account:

    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #making private variable that cannot be accessed by outside the class...

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
#print(acc1.__acc_pass).........It will give error therefore we cannot print it outside the class..
print(acc1.reset_pass()) #It won't give u error...

class Person:
    def __hello(self): #Private method...cannot be called from outside the class but can be called from inside the class through different function...
        print("Hello everyone")

    def welcome(self):
        self.__hello()

P1 = Person()
P1.welcome()