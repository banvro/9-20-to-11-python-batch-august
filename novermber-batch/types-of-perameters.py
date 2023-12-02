# function : 

# def myfun(a, b):
#     c = a + b
#     print(c)
    
# myfun(10, 20)


# Types of perameters : 
#     1) postional perameters
#     2) Keyword perameters
#     3) Default perameters
#     4) Veriable Length perameters
#         1) *args
#         2) **kwargs


#  1) postional perameters

# def sumthis(a, b, c):
#     print(c)
#     x = a + b + c
#     print(x)
    
# sumthis(12, 10, 89)


# 2) Keyword perameters

# def savaeinfo(x, y):
#     print(f"user name is {x} and user age is {y}.")

# savaeinfo(y = 20, x = "kriss")


#     3) Default perameters


# def sumthis(a = 0, b = 0, c = 0):
#     x =a + b + c
#     print(x)

# sumthis()



# 4) Veriable Length perameters
#         1) *args : arbitrary postionl arguments
#         2) **kwargs : keywrod arbitrry postioanl arguments


# def sumthis(*x):
#     totle = 0
#     for i in x:
#         totle = totle + i
    
#     print(totle)
    
# sumthis(10, 20, 20, 89)



def saveinfo(**x):
    print(x)

saveinfo(name = "kriss", age = 89)






