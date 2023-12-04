# def xyz(a, b):
#     x = a + b
#     print(x)
    
# xyz(12, 10)


# 1) postional perameters
# 2) default perameters
# 3) keyword arguments
# 4) veribale length permeters:
#     1) *args
#     2)**kwargs



# def xyz(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#     x = a + b
#     print(x)


# xyz(12, 10, 90)






# def userinfo(x, y):
#     print(f"user name is {x} and user age is {y}")


# userinfo("moris", 20)

# userinfo("kriss", 50)

# userinfo(y = 20, x = "kriss")




# 2) default perameters


# def sumthis(x = 0, y = 0, z = 0):
#     c = x + y + z
#     print(c)


# sumthis(12, 1, 2)






# 4) veribale length permeters:
#     1) *args => arbitrary posational arguments

#     2)**kwargs : keyword arbitrary postaional arguments


# def sumthis(*x):
#     print(x)
#     zx = 0
#     for i in x:
#         zx = zx + i
#     print(zx)


# sumthis(12, 10, 10, 89, 67, 1)



# def saveuserdetai(**x):
#     print(f'''username is : {x["name"]}, 
#         age is{x["age"]}
#         number is : {x["number"]}''')



# saveuserdetai(name = "kriss", age = 20, number = 9283938264)

a = "this is a car"

a.count("i")

