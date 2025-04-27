# Static methods - Methods that don't use the self parameter (work at class level)

class Student:

    @staticmethod #A decorator
    def college():
        print("ABC College")

#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

s1 = Student()
s1.college()