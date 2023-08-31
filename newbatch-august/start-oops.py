# # OOps: object oriented programming lanaguage..

# # topics : 
# 1) class
# 2) object
# 3) self
# 4) attributes
# 5) constructer

# 6) inharitance
#     1) simple inharitance
#     2) mutlipal inharitance
#     3) multilavel inharitance
#     4) hirarical inharitance
#     5) Hibried inharitance
    
# 7) Encapsulation
#     access spaifires
#         1) private
#         2) protected
#         3) public
        
# 8) Ploymorphisum:
#     method overloadding
#     metgid overrifing
#     operator overloading
#     duck typing

# 9) abstraction


# oops:

# object : instance of a class

# class : blupreint of an object

# self : used for refrencing....

# constructer : call automaticlly while object craeete of an clas



# crate a class using keyword class..:

# class xyz:
#     def mthd1(self):
#         print("i am form class xyz and mthd 1")
    
#     def mthd2(self):
#         print("i am from mthd 2 and from class xyz")
        
# objxyz = xyz()

# objxyz.mthd2()

# objxyz.mthd1()




# constructer : can be created using __init__ method

class clas1:
    def __init__(self, a, b):
        # print("i am a constructer..")
        self.name = a
        self.age = b
    
    def myinfo(self):
        print(f"my name is {self.name} and my age is {self.age}")
    
    def car(self):
        print("i am a car")
    
    def bus(self):
        print("i am a bus")
    
    def truck(self):
        print("this is a truck...")
        
# obj = clas1()
# obj.car()


# obj = clas1("kriss", 20)
# obj.myinfo()

# obj1 = clas1("moris", 21)
# obj1.myinfo()






