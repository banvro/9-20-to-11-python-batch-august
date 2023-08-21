# decleation of function

# call a function

# function perameters

# 1) Parameters
# 2) Arguments

# perameters
# def sum(a, b):
#     c = a + b
#     print(c)


# sum(12, 10)

# sum(100, 200)

# sum(90, 20)


# Perameters:
    # 1) Postatinal Permeters
    # 2) Default Perameters
    # 3) Keywaord named perameters
    # 4) Variable Length Perameters

# 1) Postatinal Permeters :

# def xyz(name):
#     print(f"my name is : {name}")
    
# xyz("kriss")
# xyz("Moris")
# xyz("myname")

# 2) Default Perameters : 

# def sumthis(x = 10, y = 20):
#     c = x + y
#     print(c)
    
# sumthis(120, 1)


# 3) Keywaord named perameters : 


# def userinfo(name, age):
#     print(f"Username is : {name} and his age is : : {age}")
    

# userinfo(age = 20, name = "kriss")

# 4) Variable Length Perameters
        # 1) *args
        # 2) **kwargs
        
        
# *args = arbitrary arguments (non-keywork arguments)
# def sumthisnow(*args):
#     # c = a + b
#     # print(c)
#     out = 0
#     print(args)
#     for i in args:
#         out = out + i
    
#     print(out)
        

# sumthisnow(12, 20, 40, 90, 10, 1)

# keyword arbitrary arguments

# kwargs

# def userindo(**kwargs):
#     # print(kwargs)
#     for i in kwargs:
#         print("u")


# userindo(name = "moris", age = 30)



# 3) Retuen


# def sum(a, b):
#     c = a + b
#     # print(c)
#     return c

# ru = sum(12, 10)


# z = ru + 10

# print("total sum : ", z)


# variable scope and lifetime

# c = 80   # global variable

# def newfun(a, b):
#     global c
#     c = a + b   # local varibales
#     print(c)

# newfun(12, 10)


# print(c)


# Anonymous function 

# lambda function

# xy = lambda arguments : expression

xyz = lambda a, b : a + b

print(xyz(100, 200))

print(xyz(40, 90))



def newfunn(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
   
 
newfunn(12, 2, 34, 90, 100, 500, 20, 65, 150, name = "kriss", age = 30, address = "i am address")










