# print(abs(-4))
# # pow ()
# print(pow(2,3))

# # type()
# a=4.5
# print(type(a))

# # int() fload str,
# print(int(5.6))
# # min(),max()
# print(min([1,2,3,4,5]))
# print(max([1,2,3,4,5]))

# # round()
# a=22/7
# print(round(a,2))

# # divmod() return  tuple  x//y x%y
# divmod(5,2)
# # bin /oct/hex 
# print(bin(4))
# # id() show address of variable in memory
# a=5
# print(id(a))
# # ord ()
# print(ord("A"))
# #len()
# print(len([1,2,3,]))

# # sum()
# print(sum((1,2,3,4)))
# # help() return the details of any function
# help("sum")
# all()
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
# print(all(iterable=[1,2,3,4,5]))

#1. any() return true if any value true
# mylist=[0,1,0]
# a=any(mylist)
# print(a)

#2. char()
# a=chr(97)
# print(a)
# 3 callable()
# def x():
    # x=5
# print(callable(x))

#  4 @classmethod()
# 5 compile()
# x = compile('print(55)\nprint(88)', 'test', 'exec')
# exec(x)

# 6 complex() return complex  number
# x=complex(2,5),complex("2+5J")
# print(x)

# 7 delattr() delete specified attribute from specified object 
# class Test:
#     name="abc"
#     age=21
#     city="indore"
# delattr(Test,"age")
# # 8.getattr() get the value of the attribute
# class Test:
#     name="xyz"
#     age=22
#     city="dewas"
# x=getattr(Test,"name")
# print(x)
# # 9.hasattr() return true false
# class Test:
#     name="zxyz"
#     age=23
#     city="bhopal"
# b=hasattr(Test,"country")
# print(b)
# # 10. setattr() set the vlue of the specific attribute
# class Test:
#     name="neha"
#     age=24
#     country="india"
# setattr(Test,"name","abc")
# x=getattr(Test,"name")
# print(x)

#11 dict() convert  creates  a dictionry 
# x=dict(name="abc",age=21,city="indore")
# print(x)

# # 12 enumrates() returnss a  enumrate object ,itrable must be sequence n return tuples
# mylist=["spring","sammer","fall", "winter"]
# a=list(enumerate(mylist))
# b=tuple(enumerate(mylist,start=1))
# print(a)
# print(b)

# def enumerate(iterable, start=0):
#     n = start
#     for elem in iterable:
#         yield n, elem
#         n += 1
# x=list(enumerate(['Spring', 'Summer', 'Fall', 'Winter']))
# print(x)

#eval() return expression of python code
# x="print(55)"
# eval(x)

# x=1
# eval("x+1")

# filter() filter the elements, itrates
# age=[12,25,35,18,20,32,15,17]
# def myfunc(x):
#     if x<=18:
#         return False
#     else:
#         return True
# a=filter(myfunc,x)
# for x in a:
#     print(x)

# def fun(x):
#     if x>5:
#         return x
# y=filter(fun,(1,2,6,8))
# for x in y:
#     print(x)

# a=filter(None,(1,0,6))
# b=filter(None,(1,0,6,True,True,False))
# a=list(a)
# b=list(b)
# print(a)
# print(b)

# def mod(x):
#     if x%3==0:
#         return x
# y=filter(mod,(12,3,45,9,6,11,8))
# for x in y:
#     print(x)

#format() format value of specifiec format
# x=format(0.8,"%")
# print(x)
# x=format(231,"d")
# print(x)
# y=format(123,"f")
# print(y)
# z=format(123,"b")
# print(z)

# frozenset() return immutable  with unique values
# l=["geek","for ","geek","is","best"]
# a=frozenset(l)
# print("frozenset is:",a)

# d={"name":"geek","age":20,"city":"indore"}
# x=frozenset(d)
# print("forzenset is:",x)

#global()
# x=globals()
# print(x)
# print("global is:",x["__file__"])

# hash() return hash value 
# a=hash(21)
# print(a)
# b=hash(22.1)
# print(b)
# c=hash(("absbhsjkkw"))
# print(c)

#help()
# a=help(sum)
# print(a)
# hex()
# print(hex(222))
# input() allow the user input
# print('Enter your name:')
# x = input()
# print('Hello, ' + x)

# int() return integer value 
# a=10
# b=10.5
# c="284"
# print(type(a),type(b),type(c))
# a=int(a)
# b=int(b)
# c=int(c)
# print(type(a),type(b),type(c))
# print(a,b,c)
# val1 = 0b010 # binary   
# val2 = 0xAF  # hexadecimal  
# val3 = 0o10  # octal  
  
# # Calling int() function   
# val4 = int(val1)   
# val5 = int(val2)   
# val6 = int(val3)   
# # Displaying result  
# print("Values after conversion:",val4, val5, val6)  
# print("and types are: \n ", type(val4), type(val5), type(val6))  

# isinstance() it returns a true value if object belongs to a class else false
# a=10
# lst=[1,3,4,5,7]
# s="ndkfjhw"
# print(isinstance(a,int))
# print(isinstance(lst,list))
# print(isinstance(s,str))
# print(isinstance(lst,tuple))

# class Student:
#     id=101
#     name="john"
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
# student=Student(1010,"john")
# lst=[1,2,3,4,23,45,32]
# print(isinstance(student,Student))
# print(isinstance(lst,Student))

# class NumericList(list):  
#     def __init__(self):  
#         return None  
  
# num = NumericList()  
# # Calling function   
# print(isinstance(num, NumericList)) # True  
# print(isinstance(num, list)) # True  

################################################################
#isssubclass() return true if class is  a subclass of classinfo
# class Myclass:
#     name="john"
# class Myinfo(Myclass):
#     age=36
#     name=Myclass
# x=issubclass(Myinfo,Myclass)
# print(x)

# iter() return iterator object
# x = iter(["apple", "banana", "cherry"])
# print(next(x))
# print(next(x))
# print(next(x))
# len() returns (length) the number of item 
# x=[1,23,45,67]
# print(len(x))
# x="yogita"
# print(len(x))
# locals() return local symbol table as dictionary .info about the current program
# x=locals()
# print(x["__file__"])
#

#map() execute specified function for each  item an itrable
# def myfun(a,b):
#     return a+b
# x=map(myfun,("yogita","solanki","neha"),("john","thomas","elvis"))
# print(x)
# print(list(x))

# def myfun(x):
#     return len(x)
# x=map(myfun,("yogita","solanki","neha"))
# print(list(x))
#
# # memoryview() return memoryview object
# x=memoryview(b"Hello")
# print(list(x))
# print(x[0])
# print(x[1])

#object() return a new featurless object
# open() the open function open a file with the given mode r w a 
# f=open("hello.txt" ,"r")
# print(f.read())

# property() return a property attribute
#range() return a sequence of number 
# x=range(1,19,2)
# for n in x:
#     print(n)
# repr() return readable version of an object 

 #reversed()  return reverse the iterator object
# alph = ["a", "b", "c", "d"]
# ralph = reversed(alph)
# for x in ralph:
#   print(x)

#slice() slice the sequence of objects
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(3, 5)
# print(a[x])

#sorted() return sorted list,sort asce/desc order
# lst=[23,56,89,21,34,567,65]
# t=(356,3,35,87,43,13)
# d={5:"five",8:"eight",1:"one",4:"four",2:"two",3:"three"}
# l=sorted(lst,reverse=True)
# tu=sorted(t)
# di=sorted(d)
# print(l)
# print(tu)
# print(di)
# li = [(2,15),(3,5),(65,5),(8,5)]  
# s=sorted(li,key=lambda x:sum(x))
# print(s)

#staticmethod()	Converts a method into a static method
# super() function is used to give access to methods and properties of a parent or sibling class.
# class Parent:
#     def __init__(self,txt):
#         self.message= txt
#     def printmasssge(self):
#         print(self.message)
# class Child(Parent):
#     def __init__(self, txt):
#         super().__init__(txt)

# x=Child("hello super function")
# x.printmasssge()

 #vars() return dict proprty (attributes) of an object
# class Person:
#     name="john"
#     age=20
#     city="mumbai"
# x=vars(Person)
# print(x)

# zip() return iterator of tuples
# for item in zip([1,2,3],("abc","yogi","xyz")):
#     print(item)

# l=[1,2,56,8,9,12]
# l1=["gdd","sdf","xyz","gds"]
# x=tuple(zip(l,l1))
# print(x)

# zip() in conjunction with the * operator can be used to unzip a list:
# x = [1, 2, 3]
# y = [4, 5, 6]
# x=list(zip(x, y))
# print(x)
# # [(1, 4), (2, 5), (3, 6)]/
# x2, y2 = zip(*zip(x, y))
# x == list(x2) and y == list(y2)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# print(len(list1))
# list2 = list1[2]
# list3 = list2[2]
# list3.append(7000)
# print(list1)
