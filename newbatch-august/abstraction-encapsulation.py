# Inharitance :

# Abstraction : data hiding

# abc = abstract base class 


# 1) ABC
# 2) abstractmethod

# from abc import ABC, abstractmethod

# class xyz(ABC):
#     @abstractmethod
#     def username(self):
#         pass
    
#     @abstractmethod
#     def mobil(self):
#         pass

# class pqr(xyz):
#     def age(self):
#         print("i am age...")

#     def username(self):
#         print("i am usernmaee....")
    
#     def mobil(self):
#         print("i ma mobile")
# obj = pqr()

# obj.username()


# obj = xyz()




# Encapsulation : wrap importnt menthod in a single units is call encapsulation...

# Access spacifires 
    # 1) public mambers
    # 2) protected mambers   _
    # 3) private mambers    __

# property
# getattr
# setattr
# delattr



# class savedata:
#     def __init__(self, a, b):
#         self.__name = a
#         self.age = b
    
#     def userdetail(self):
#         print(f"username is {self.__name} and age is {self.age}.")

# class newdata(savedata):
#     def userdetail(self):
#         print(f"usernme is {self.__name}")


# obj = newdata("moris", 20)
# obj.userdetail()
# print(obj.__name)













