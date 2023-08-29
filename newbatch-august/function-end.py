# Functions 

# lambda function

# lambda arguments : expession


# def sumthis(a, b):
#     c = a + b
#     print(c)

# sumthis(12, 10)

# zx = lambda a, b : a + b

# print(zx(100, 200))

# ey = lambda 

# def sq(a):
#     z = a ** 2
#     print(z)
    
# sq(10)

# asr = lambda a : a ** 2

# print(asr(90))

# map()
# filter()
# reduce()

# a = [12, 20, 100, 200, 90, 40]

# # map()
# # map(function, itreater)

# qw = map(lambda x : x + 20, a)

# print(list(qw))

# qw = [1, 2, 3, 4, 5, 7, 8]

# zx = map(lambda x : x ** 2, qw)

# print(list(zx))

# filter 

# a = [12, 23, 10, 90, 78, 100, 78, 3, 11]

# # filter(function, itrater )

# zx = filter(lambda x : x%2 != 0, a)

# print(list(zx))


# from functools import reduce

# a = (1, 2, 3 ,4, 5, 6,7 , 8)

# zx = reduce(lambda a, b : a + b, a)

# print(zx)







# def abc(a, b):
#     c = a + b
#     return c
    
# zx = abc(12, 10)


# print(zx)




# clasures :

# def outer_fun(a):
#     def inner_fun(b):
#         return a + b
#     return inner_fun

# zx = outer_fun(100)

# x = zx(200)
# print(x)




# partial function 

# from functools import partial

# def sumthis(a, b):
#     c = a + b
#     print(c)

# zx = partial(sumthis, b = 100)

# zx(500)

# sumthis(12, 10)



# DRY  


# c = 20

# def sumthis(a, b):
#     c = a + b
#     return c

# qw = sumthis(100, 200)
# print(qw)
# print(c)


# recursion  


# factoial 

# 5!

# 5x4x3x2x1


def factorl(n): #4
    if n <= 0:
        return 1
    else:
        return n * factorl(n-1) 


print(factorl(4))







