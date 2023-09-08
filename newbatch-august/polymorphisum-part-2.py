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
























    
    
    
    
    
    
    
    
    
    
    
    

