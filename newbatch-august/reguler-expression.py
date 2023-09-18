# import re

# txt = "Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's  a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[47][48] Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[51]"

# ptrn = "in"

# mtch = re.search(ptrn, txt)

# print(mtch)



# import re

# text = "Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his  from his responsibilities as Python's , a title the Python community bestowed upon him 4172815605 to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a 872510783645  five-member Steering Council to lead the project.[47][48] Python 2.0 was released on 16 October 2000, with many major new 9182638452 features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, 9263619856 released on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of Python 3 include the 2to3 utility, which 9164539457 automates the translation of Python 2 code to Python 3.[51]"

# # ptrn = "\d{10}"
# ptrn = "[89]\d{10}"
# # ptrn = "\d\d\d\d\d\d\d\d\d\d"


# mtch = re.findall(ptrn, text)
# # mtch = re.finditer(ptrn, text)
# print(mtch)

# # for i in mtch:
# #     print(i)


# import re 

# text = "Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his  from his pqr_123@gmail.com responsibilities as Python's , a title the Python community bestowed upon him 4172815605 to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a 872510783645  five-member Steering Council to lead the project.[47][48] Python 2.0 was released on 16 October 2000, with many major new 9182638452 features such as list comprehensions, abc@gmail.com cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, 9263619856 released xyz123@gmail.com on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of qiwet@gmail.in Python 3 include the 2to3 utility, which 9164539457 automates the  pqr.extech123@gmail.com translation of Python 2 code to Python 3.[51]"

# p = "[a-zA-Z0-9_\-\.]+[@][a-z]{5}\.[a-z]+"


# mtach = re.findall(p, text)

# print(mtach)





import re

txt = "Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his  from his pqr_123@gmail.com responsibilities as Python's , a title the Python community bestowed upon him 4172815605 to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a 872510783645  five-member Steering Council to lead the project.[47][48] Python 2.0 was released on 16 October 2000, with many major new 9182638452 features such as list comprehensions, abc@gmail.com cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, 9263619856 released xyz123@gmail.com on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of qiwet@gmail.in Python 3 include the 2to3 utility, which 9164539457 automates the  pqr.extech123@gmail.com translation of Python 2 code to Python 3.[51]"



ptrn = "[^a-zA-Z0-9]"

xyz = re.findall(ptrn, txt)
# print(xyz)


lst = []

for i in xyz:
    if i == " " or i == ".":
        continue
    lst.append(i)

print(lst)
