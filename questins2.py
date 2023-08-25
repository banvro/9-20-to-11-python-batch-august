# # a = 10

# # a = a + a + a 

# # print(a - len('car'))


# # 1, 2, 4, 7, 11, 16, 22, 37



# a = 0
# b = 1
# lt = []

# while a < 30:
#     # print(a)
#     lt.append(a)
#     c = a + b
#     a = b
#     b = c

# print(lt)
    

# 1, 2, 4, 7, 11, 16, 22, 37

# a = 1
# lt = []
# for i in range(1, 10):
#     lt.append(a)
#     a = a + i
    
# lt.remove(29)   
# print(lt)

a = 1
b = 1
lt = []
while True:
    # if a < 38:
        # print(a)
    lt.append(a)
    a = a + b
    b = b + 1
    if a > 40:
        break       
    
print(lt)



# [1, 11, 111, 1111, 11111, 111111]

a = "1"
la = []
for i in range(1, 6):
    b = a * i
    la.append(int(b))
    # print(b)

print(la)




    
    
    
    
    
    
