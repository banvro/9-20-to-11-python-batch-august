# # class
# # object
# # self
# # constructer
# # attributes

# # Inharitance : 
    
# # single inharitance
    
# # class cls1:
# #     def mthd1(self):
# #         print("i am from class 1")
    
# #     def mthd2(self):
# #         print("i am form class1 and mthd 2")
        
        
# # class cls2(cls1):
# #     def mthd3(self):
# #         print("i am from class 2 and mehtd 3")

# # obj = cls2()
# # obj.mthd1()

# # obj1 = cls2()
# # obj1.mthd1()


# # 1) Single inharitance
# # 2) Multipal inharitance
# # 3) multilevel inharitance
# # 4) hirerachical inharitnace
# # 5) hybrid Inharitance

# #  Multipal inharitance   
# # class cls1:
# #     def mthd1(self):
# #         print("i am from class 1")
    
# #     def mthd2(self):
# #         print("i am form class1 and mthd 2")
        
# # class cls2:
# #     def mthd3(self):
# #         print("i am from class 2 and mehtd 3")

# # class cls3(cls1, cls2):
# #     def mthd4(self):
# #         print("i am from class 3")

# # obj = cls3()




# # multilevel inharitance


# # class cls1:
# #     def mthd1(self):
# #         print("i am from class 1")
    
# #     def mthd2(self):
# #         print("i am form class1 and mthd 2")
        
# # class cls2(cls1):
# #     def mthd3(self):
# #         print("i am from class 2 and mehtd 3")

# # class cls3(cls2):
# #     def mthd4(self):
# #         print("i am from class 3")

# # obj = cls3()
# # obj.mthd1()
# # # obj.mthd1()


# # hirerachical inharitnace



# class cls1:
#     def mthd1(self):
#         print("i am from class 1")
    
#     def mthd2(self):
#         print("i am form class1 and mthd 2")
        
# class cls2(cls1):
#     def mthd3(self):
#         print("i am from class 2 and mehtd 3")

# class cls3(cls1):
#     def mthd4(self):
#         print("i am from class 3")
        
# class cls4(cls2, cls3):
#     pass

# obj = cls4()
# obj.mthd1()
# # obj.mthd1()



# super()

class cls1:
    def __init__(self, a, b):
        self.name = a
        self.age = b
        
    def saveinfo(self):
        print(f"user name is : {self.name} and age is : {self.age}")

# obj = cls1("abc", 20)
# obj1 = cls1("xyz", 60)
# obj.saveinfo()
# obj1.saveinfo()

class cls2(cls1):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.phone_number = c
        
    def saveinfo(self):
        print(f"user name is : {self.name} and age is : {self.age} and user phone number is : {self.phone_number}")

obj = cls2("avc", 20, 918623981)
obj.saveinfo()











