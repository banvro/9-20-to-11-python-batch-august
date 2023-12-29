import threading

def fun1():
    for i in range(1, 101):
        print("heyyyyyyyyyyyyyyy")

def fun2():
    for i in range(1, 101):
        print("noooooooo")
    
# fun1()
# fun2()

th1 = threading.Thread(target = fun1)
th2 = threading.Thread(target = fun2)     

th1.start()
th2.start()

print("this is importatnt code")

print("i am workng")

print("process...")

th1.join()
th2.join()

print("dnee")


# a = 10
# b = 20
# c = a + b

# d = c + 90

# print(d)