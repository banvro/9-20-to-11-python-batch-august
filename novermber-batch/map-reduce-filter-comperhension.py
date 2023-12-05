# L

# x = lambda a, b : print(a + b)

# x(10, 20)

# 1) map()
# 2) filter()
# 3) reduce()


# 1) map()

# lst = [10, 20, 90, 78, 67, 100, 78]

# # map(lambda funcation, itrater)

# x = map(lambda x : x + 10, lst)

# print(list(x))




# lst = [2, 3, 3, 5, 2, 3, 4, 1, 2, 10]

# c = map(lambda q : q ** 2, lst)

# print(tuple(c))


# a = "this is car "

# d = map(lambda e : e + "10", a)

# print(list(d))


# 2) filter : 

# a = "2837642374238457"





# for i in a:
#     print(i)



# lst = [1, 4, 2, 3, 1, 4, 2, 6, 5, 7, 5, 2, 3, 4, 12, 10, 11]

# # filter(lambda funcation , itrater)


# zx = filter(lambda r : r % 2 == 0, lst)

# print(list(zx))






# 3) reduce:

# reduce(lambda funcation, itrater)

# from functools import reduce

# lst = [1, 9, 2, 3 ,4, 17, 6]

# zx = reduce(lambda a, b : a + b, lst)


# print(zx)




# Comperhension : 

# 1) List


# [expression, loop, condation]


# l = [i for i in range(1, 11) if i % 2 == 0]

# print(l)

# a = []

# for i in range(1, 11):
#     a.append(i)

# print(a)







# a = int(input("Enter numbber"))


# print(a)



# choic = int(input("Enter how manay inputs you wana enter : "))

# lst = [int(input(f"Enter {i+1} number : ")) for i in range(choic)]

# print(lst)




["2 x 1 = 2", "2 x 2 = 4", .. . . . . . . . ...  . . .]




