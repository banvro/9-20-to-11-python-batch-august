# class xyz:
#     def __init__(self):
#         self.name = "kriss"
#         self.age = 20
    
#     def cr(self):
#         print("heyyyyyyyy")
        
        
# obj = xyz()
# print(obj.name)

# del obj 
# # obj = None

# print(obj.name)


# Generator 
# yield
# one the fly 

# a = [1, 2, 3, 4, 6]

# for i in a:
#     print(i)

# def xyz(n):
#     for i in range(n):
#         yield i

# pq = xyz(6)

# print(next(pq))
# print(next(pq))

# x = [1, 2, 3, 4]

# z = iter(x)

# print(next(z))
# print(next(z))



# iter()

# next()

# a = [1, 2, 3, 4, 6]

# zx = iter(a)

# print(next(zx))
# print(next(zx))
# print(next(zx))
# print(next(zx))

# range()

class myiterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.start <= self.end:
            zx =  self.start
            self.start += 1
            return zx
        else:
            raise StopIteration
        
obj = myiterator(1, 5)

for i in obj:
    print(i)






# a = 10

# a += 2
# a = a + 2

# print(a)























