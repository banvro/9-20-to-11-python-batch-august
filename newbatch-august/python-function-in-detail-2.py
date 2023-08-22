#     # lambda function

#     # lambda arguments : expression 

#     # zx = lambda a : a + 2

#     # print(zx(12))

#     # map()

#     # map(function, intrater)

#     # a = [1, 2, 3, 4, 6, 7, 10]


#     # zx = map(lambda x : x + 2,  a)

#     # za = list(zx)

#     # print(za)

#     # filter()

#     # filter(funcation, intrater)

#     # a = [2, 3, 1, 4, 5, 7, 10, 21, 23, 26]

#     # zx = filter(lambda x : x // 2 == 0, a)


#     # 2.6

#     # print(list(zx))

#     # reduce()  => 

#     # functools

#     # from functools import reduce

#     # a = [1, 2, 3, 4, 6, 1]

#     # zx = reduce(lambda x, y : x + y, a)

#     # print(zx)







# a = [23, 100, 46, 90, 30, 45, 32, 98]
# print(a)

# # +  10

# za = map(lambda x : x + 10, a)
# # print(list(za))
# aw = list(za)
# # /2

# print(aw, 'iiiiiiii')

# xs = filter(lambda k : k % 2 == 0, aw)
# # print(list(xs))
# # for i in xs:
# #     print(i)
# io = list(xs)
# print(io)
# # ++
# print(io, "yyyyyyyyyyyyyyyyyyyy")

# from functools import reduce

# yu = reduce(lambda x, y : x + y, io)

# print(yu)






# function dacorator 

# function dacoratoers

def decot(fun):
    def waper(*args, **kwargs):
        print("weclome to my function ...this helps you alott...lets go")
        
        fun(*args, **kwargs)
        
        print("thank you for using me...")
        
    return waper

@decot
def syi(a, b):
    c = a + b
    print("output = ", c)
    
# syi(100, 200)


@decot
def ui():
    print("nooo")
    
ui()
