# OOP's

# Abstraction  : 
#     absreact class
#     abstract method
#     interfaces
    
# abc = abstract base class


from abc import ABC, abstractmethod

class basestructer(ABC):
    @abstractmethod
    def privacy_policy(self):
        pass
    
    @abstractmethod
    def faqz(self):
        pass
    
    def homepage(self):
        print("this is home page")


class ActulApp(basestructer):
    def startproject(self):
        print("we start to create project")
        
    def privacy_policy(self):
        print("this is privacy policy")

obj = ActulApp()
obj.startproject()







