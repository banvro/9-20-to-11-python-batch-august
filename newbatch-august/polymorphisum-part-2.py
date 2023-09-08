# polymorphism : 
    # 1) Complile time polymorpism
    #     a) Method overloading
    #     b) operator overloading
    
    # 2) Run time polymorphism
    #     a) method overriding
    #     b) interfaces
    
    # Duck Typing..
    
# method overloading:

# class cls1:
#     def show(self,a , b, c):
#         print(a  + b + c)
    
#     def show(self, a, b):
#         print(a + b)
    
#     def show(self, a):
#         print(a)
    
# obj = cls1()

# obj.show(12, 19)



# class cls1:
#     def show(self, *args):
#         # print(args)
#         totl = 0
#         for i in args:
#             totl = totl + i
#         print(totl)
# obj = cls1()

# obj.show(12, 100, 1)


# Duck typing : 

class cls1:
    def mthd(self):
        print("i am form class 1")

class cls2:
    def mthd(self):
        print("i am fri class 2")
        
obj1 = cls1()
obj2 = cls2()

# obj2.mthd()

def qw():
    # print(q)
    # q.mthd()
    obj1.mthd()

qw()








# # 10 + 30

# # a + b

# # operends

# # operators : 

# # +, -, *, /


# # operatoer overloading : 




# # 10 + 20

# # a = 10

# # b = "20"

# # print(a + b)


# class xyz:
#     def __init__(self, a, b):
#         self.num1 = a
#         self.num2 = b
    
#     def __add__(x, y):
#         a = x.num1 + y.num1
#         b = x.num2 + y.num2
#         sum = xyz(a, b)
#         return sum
    
# obj = xyz(12, 90)
# abc = xyz(10, 20)

# zx = obj + abc

# print(zx.num2)



class xy:
    def __init__(self, a, b):
        self.name = a
        self.age = b

    def save(self):
        print(self.name, self.age)

obj = xy("moris", 10)
obj1 = xy("kriss", 20)
obj2 = xy("tk", 70)

class yz(xy):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.phone_number = c

    def save(self):
        print(self.name, self.age, self.phone_number)


newobj = yz("muname", 20, 891263)

newobj.save()
































    
    
    
    
    
    
    
    
    
    
    
    

