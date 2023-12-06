# Decorator : 


# def dectorr(fun):
#     def wrper():
#         print("welcom to my funcation")
#         fun()
        
#         print("thannk you for using my funcation")
#     return wrper()

# @dectorr
# def sumthis():
#     print("this is main funcation")
    
# # sumthis()

# @dectorr
# def xyz():
#     print("hlooooooooooooooooo")
    

# # xyz()
    
    
    
# def mydecorator(x):
#     def wp(*args, **kwargs):
#         print("lets start, this ::::::::")
        
#         x(*args, **kwargs)
        
#         print("thnk you for using me....")   
#     return wp
    
# @mydecorator
# def sumthis(a, b):
#     x = a + b
#     print(x)
    
# sumthis(12, 10)
    
# @mydecorator    
# def sumthisall(a, b, c):
#     x = a + b + c
#     print(x)

# sumthisall(12, 10, 20)
    
    



# Recursion : when a funcation calling itself and fall in a infinite loop

# def car():
#     print("hello")
#     car()


# car()


# factoril : 

# 4 = 4 x 3 x 2 x 1 = 24
# 3 = 3 x 2 x 1 = 6


# def factroil(x):
#     if x < 1:
#         return 1
#     else:
#         return x * factroil(x-1)
#             # 4 * factroil(3)
#             #      3 * factroil(2)
#             #           2 * factroil(1)
#             #               1 * factroil(0)
#             #                   0 * factroil(-1)

# x = factroil(3)
# print(x)



# fabnoci series:
    
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34



    
    
