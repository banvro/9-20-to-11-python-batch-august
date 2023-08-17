# import re

# tet = "kzjbasbdbasbdkjasjbd9283498236 kagkabdkjasdbkjajdkas 7352836492 akjhdvjhasdad 9123798214"


# ptrn = "\d{10}"

# match = re.findall(ptrn, tet)

# print(match)


# a = sfbf* hsdf + 8923

# print(12 + 30)

# print('done')

# import threading


class xyz:
    def car(self):
        for i in range(0, 12):
            print("carrrr")



# class abc:
#     def bus(self):
#         for i in range(0, 12):
#             print("busssssss")

# obj1 = xyz()
# obj2 = abc()

# obj1.car()
# obj2.bus()



import threading

class xyz:
    def car(self):
        for i in range(0, 120):
            print("carrrr")

class abc:
    def bus(self):
        for i in range(0, 120):
            print("busssssss")

obj1 = xyz()
obj2 = abc()

# obj1.car()
# obj2.bus()

th1 = threading.Thread(target=obj1.car)
th2 = threading.Thread(target=obj2.bus)


th1.start()
th2.start()



th1.join()
print("ooooooooooooooooooo")