# Encapsulation : 


# class cls1:
#     def __init__(self, x, y):
#         self.a = x
#         self.b = y

#     def __mthd1(self):
#         print("ok")
    
#     def methd2(self):
#         print("car")
    
#     def mthd3(self):
#         print("arioplain")
        
# class cls2(cls1):
#     def xyz(self):
#         print(self.a)


# obj = cls2(10, 20)

# obj.xyz()
# public 
# private 
# protected


# property
# getter
# setter
# deleter

# abc = map(fauction, itterater)

# class cls1:
#     def __init__(self, x, y):
#         self.name = x
#         self.age = y
    
#     def xyz_name(self):
#         return self.name
    
#     def setter_x(self, new_age):
#         self.age = new_age
        
#     def delter(self):
#         del self.age
    
#     def __str__(self):
#         return f"usernmae is {self.name} and age is {self.age}"


# obj = cls1("moris", 20)
# print(obj.xyz_name())
# obj.setter_x(90)
# # obj.delter()

# print(obj)




class cls1:
    def __init__(self, x, y):
        self.name = x
        self.age = y
    
    def age(self):
        return self.age
    
    def __str__(self):
        return f"usernmae is {self.name} and age is {self.age}"
       
       
       
obj = cls1("kriss", 20)


print(obj)







class cls1:
    def __init__(self, x, y):
        self.name = x
        self._age = y
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age 
        else:
            return "please enter valid age..."
    
    def __str__(self):
        return f"usernmae is {self.name} and age is {self._age}"
       
obj = cls1("kriss", 20)

obj.age = 100

print(obj)
