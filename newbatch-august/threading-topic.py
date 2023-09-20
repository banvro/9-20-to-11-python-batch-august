# a = 20

# b = 30

# c = a + b

# print(c)

# print("hello")

# print("xyz")

# print("still code runnning...")

# print("noooo")

# print

# import threading


# a = 20

# # b = 30

# # c = a + b

# # print(c)

# # for i in range(100):
# #     print("Hello world")

# # print("xyz")

# # print("still code runnning...")

# # print("noooo")

# # 1) Process

# # 2) Threads


# class xyz:
#     def mthd1(self):
#         for i in range(200):
#             print("yesssss")
        
#     def mthd2(self):
#         for i in range(200):
#             print("nooooooooooo")

# obj = xyz()

# obj.mthd1()
# obj.mthd2()

# print("i am  runnninggg...")

# print("new process")

# print("this is importnt code")

# print("done.")

import threading

class xyz:
    def mthd1(self):
        for i in range(200):
            print("yesssss")
        
    def mthd2(self):
        for i in range(200):
            print("nooooooooooo")

obj = xyz()

def car():
    for i in range(10):
        print("i am function...")

thred1 = threading.Thread(target = obj.mthd1)
thred2 = threading.Thread(target = obj.mthd2)
thred3 = threading.Thread(target = car)

thred3.start()

thred1.start()
thred2.start()

print("i am  runnninggg...")

print("new process")

print("this is importnt code")

thred1.join()
thred2.join()

print("done.")





# a = 10
# b = 20
# c = a + b 

# d = c + 10
# print(d)














