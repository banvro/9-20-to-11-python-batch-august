# PolyMorphism : 
    
#     poly :  many
    
#     morphism : forms


# 1) Compile time polymorphism
#     operator overloading
#     method overloading

# 2) Run time polymorphism
#     method overriding
#     interfaces

# duck typing 


# operator overloading :

# class cls1:
#     def sumthis(self, a, b, c):
#         d = a + b + c
#         print(d)
    
#     def sumthis(self, a, b):
#         c = a + b
#         print(c)
    
#     def sumthis(self, a):
#         c = a
#         print(c)

# obj = cls1()
# obj.sumthis(12)


        
    
# class cls1:
#     def sumthis(self, a = None, b = None, c = None):
#         if a != None and b != None and c != None:
#             zx = a + b + c
#             print(zx)
        
#         elif a != None and b != None:
#             zx = a + b
#             print(zx)
        
#         elif a != None:
#             zx = a
#             print(zx)
        
#         else:
#             print("Enter something..")
    
# obj = cls1()
# obj.sumthis(12, 100, 1)
   
   
# method overrriding : 

# age = 18


# age = 90


# print(age)

# class cls1:
#     def showme(self):
#         print("i am from class 1")
    
#     def ok(self):
#         print("i am ok//....")

# class cls2(cls1):
#     def no(self):
#         print("noooooooooo")
    
#     def showme(self):
#         print("i am from class 2...")
    
# obj = cls2()   

# obj.showme()
















   
   
   
   
