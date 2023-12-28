import re

text = """In February 1991, Van Rossum published the code (labeled version 0.9.0) to alt.sources.[11][12] Already present at this stage in development were classes with inheritance, exception handling, functions, and the core datatypes of list, dict, str and so on. Also in this initial release was a module system borrowed from Modula-3; Van Rossum 
abc123@gmail.in describes the module as "one of Python's major programming units".[1] Python's exception model also resembles Modula-3's, with the addition of an else clause.[3] In 1994 comp.lang.python, the primary discussion forum for Python, was formed, marking a milestone in the growth of Python's userbase.[1]askdkj@yahoo.com
+61(987)-997-973-237
Version 1
abc@gmail.com
Python reached version 1.0 in January 1994. The major new features included in this release were 9826376518 the functional programming tools lambda, map, filter and reduce. Van Rossum stated that "Python acquired lambda, reduce(), filter() and map(), courtesy of a Lisp hacker who missed them and submitted working patches".[13] +44(937)-453-785-342
abc12@gmail.com
The last version released while Van Rossum was at CWI was Python 1.2. In 1995, Van Rossum continued avx@gmail.co.inhis work on Python at the Corporation for National 8673527645 Research Initiatives (CNRI) in Reston, Virginia from where he abc123xyz@gmail.com released several versions.

By version 1.4, Python had acquired several new features. Notable among these are the Modula-3 inspired keyword arguments (which are also similar to Common Lisp's keyword arguments) and 5620925678 built-in support for complex numbers. Also included is a basic form of data hiding by name mangling, though this is easily bypassed.[14]

During Van Rossum's stay xyz.pqe123xyz@gmail.com at CNRI, he launched the Computer Programming for Everybody (CP4E) initiative, intending to make programming more accessible to more people, with a basic "literacy" in programming languages, 1234567890 similar to the basic English literacy and mathematics skills required by most employers. Python served a central role in this: because of its 9856372976focus on clean syntax, it was already suitable, and CP4E's goals bore similarities to its predecessor, ABC. The project was funded by DARPA.[15] As of 2007, the CP4E project is inactive, and while Python attempts to be easily learnable and not too arcane in its syntax and semantics, 3462810956 outreach to non-programmers is not an active concern.[16]"""


ptrn = "[6789]\d{9}"


matches = re.findall(ptrn, text)

print(matches)

# matches = re.finditer(ptrn, text)

# for i in matches:
#     print(i)


# matches = re.search(ptrn, text)

# print(matches)













