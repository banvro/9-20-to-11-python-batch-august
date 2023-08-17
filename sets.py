# set: collection of diffrent type of data 
# {}


st = {1, 2, 6, "hlo", 10.7, "car"}

# st = {"1", 2, 6, "hlo", 10.7, "car"}

# print(st)
# print(type(st))

# # []
# list : ordered, [], mutable, 
    
# tuple : oriderd, (), imputable

# set : unordered, {}, mutable, 

# dictnary  : ordered, {key:value}, mutable, 

# lt = [2, 4, 6, 7, 90]

# print(lt[3])


# lt.append("bus")

# lt.insert(1, "tree")

# print(lt)

# tl = (1, 2, 3, 4, 5, 6)



# st = {"1", 2, 6, "hlo", 10.7, "car"}


# st.add(12)

# st.remove('hlo')
# print(st)



# dictionary:  key : value paris

# {}


# dicto = {
#     "name" : "Kriss",
#     "Age" : 20,
#     "Phone_Number" : 9823928364
# }



# print(type(dicto))
# print(dicto)

# print(dicto["Age"])

# dicto["marks"] = 90


# print(dicto)


# dicto = {
#     "name" : "Kriss",
#     "Age" : 20,
#     "Phone_Number" : 9823928364
# }


# print(dicto.keys())
# print(dicto.values())

# for i in dicto.values():
#     print(i)


# dicto.remove('Age')
# remove.dicto['Age']
# dicto.pop('Age')

# print(dicto)



# ls = [4, 5, 6, 8, 10]

# ls.pop()

# print(ls)



# stack : push, pop





# tl = (4, 7, 12, 10)

# # tl.add(90)

# lt = list(tl)

# print(lt)

# lt.append("io")

# print(lt)

# tl = tuple(lt)

# print(tl)



# str = '2782323'

# lt = []

# for i in str:
#     vr = int(i)
#     lt.append(vr)

# print(lt)

# print(sum(lt))







# reguler expressions:

import re

# text
# pattrens

text = "this is my data, i love my data."

pattren = "data"


match = re.search(pattren, text)
# match = re.finditer(pattren, text)

print(match.group())