# Exception Heanding:


# try:
#     # doutable code

# except Exception:
#     # excecute only if try have an error

# else:
#     # exceute only if try code havent any error

# finally:
#     # it execute both time.


# a = 10
# b = 2

# try:
#     c = a / b

# except Exception:
#     print("here is an error")

# else:
#     print(c)

# finally:
#     print("exception heandling working")

# print("prt of code")

# print("this is imorwstn code")

# print("done")

# a = 10
# b = 0
# print(a/b)




a = 10
b = 2

try:
    c = a / b
    age = int(input("Enter your age : "))


except ZeroDivisionError:
    print("yui never devode anything by 0")

except ValueError:
    print("Enter some vaild value")
    
except Exception as e:
    print("here is an error")

else:
    print(c)
    print("User age is : ", age)

finally:
    print("exception heandling working")

print("prt of code")

print("this is imorwstn code")

print("done")
