# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructors etc
# objects for your classes


# self keyword is mandatory for calling variable name into method
# instance and class variables have whole different purpose
# constructor name should be _init_
# new keyword is not required when you create object

class Calculator:
    num = 100 # class variables
    # default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I'm called authomatically when object is created")

    def getData(self):
        print("I'm now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num



obj = Calculator(2, 3) #syntax to create objects in Python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5) #syntax to create objects in Python
obj1.getData()
print(obj1.Summation())