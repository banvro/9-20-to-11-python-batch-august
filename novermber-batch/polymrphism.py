# class mycls:
#     def __init__(self):
#         self.name = "kriss"
    
#     def __car(self):
#         print("this is a car prvate ")
        
#     def bus(self):
#         self.__car()

# obj = mycls()
# obj.bus()


# Polymorphism : when 1 thing have multiple form is called polymorphism



# 1) Compile Time polymorphism
#     1) Operator Overloaing
#     2) Method Overloading

# 2) run time polymorphism
#     1) Method Overriding



# 10 + 20

# operands = 10, 20
# operator = +

class mycls:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def car(self):
        print("this is a car")
    
    def __add__(x, y):
        q = x.num1 + y.num1
        w = x.num2 + y.num2
        summ = mycls(q, w)
        return summ

obj = mycls(10, 90)

obj1 = mycls(20, 56)

x = obj + obj1

print(x.num2)
# 10 + 90


# 10 + "hello"


