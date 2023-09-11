# # 1) Comperhension : 
# u = int(input("Enter how many numbers you want to enter : "))
# nums = [(int(input("Enter number : "))) for i in range(u)]

# print(nums)



# comperhension :

# 1) List comhension
# 2) set comperhension
# 3) dict comperhesion

# [expression itreater condation]

# a = [i  for i in range(1, 10) if i % 2 == 0 and i != 6]

# print(a)

# 2) Set comperhension :

# {key expresion : value expression itreater condation }

# a = {i * 2 : i  + 10  for i in range(1, 5)}

# print(a)

a = ["name", "age", "number"]

b = ("moris", 20, 91823691)

# output : 

{"name" : "moris", "age" : 20, "number" : 91823691}









# # 1) Comperhension : 
# u = int(input("Enter how many numbers you want to enter : "))
# nums = [(int(input("Enter number : "))) for i in range(u)]

# print(nums)



# comperhension :

# 1) List comhension
# 2) set comperhension
# 3) dict comperhesion

# [expression itreater condation]

# a = [i  for i in range(1, 10) if i % 2 == 0 and i != 6]

# print(a)

# 2) Set comperhension :

# {key expresion : value expression itreater condation }

# a = {i * 2 : i  + 10  for i in range(1, 5)}

# print(a)

# a = ["name", "age", "number"]

# b = ("moris", 20, 91823691)

# # output : 

# # {"name" : "moris", "age" : 20, "number" : 91823691}

# ac = {a[i] : b [i] for i in range(len(a))}

# print(ac)

a = "i am a python devloper, who are you"

b = ["a", "e", "i", "o", "u"]


# for i in a:
#     if i in b:
#         continue
#     print(i)

zx = [i for i in a if i not in b]

print(zx)





