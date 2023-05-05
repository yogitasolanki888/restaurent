# __init___  method 
# example
# class  Initmethod:
#     def __init__(self,p,r,t):
#         self.p= p
#         self.r =r
#         self.t =t
#     def logic(self):
#         self.si = (self.p*self.r*self.t)/100
#     def display(self):
#         print("result is : " ,self.si)
# obj=Initmethod(1000,23,2)
# obj.logic()
# # obj.p=7000
# # print(obj.p)
# # del obj.p
# obj.display()


# class Test:
#     def __init__(self,name , age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("hello my name  is " + self.name , self.age)
# obj = Test("yogi",21)
# obj.age= 22
# del obj.age
# obj.display()


# __str__  method 
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f" {self.name},{self.age}"
# p=Person("john", 32)
# print(p)

# Complete Program Explanation of Constructor and Destructor:-

# class Addition:
#     def __init__(self):
#         self.a=100
#         self.b=200
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print("result is "+str(self.a+self.b))
#     def __del__(self):
#         print("Destructor will be called")

# obj = Addition(10,20)
# obj.add()

# del obj

# static data members exaple of static data members and class type
# class A:
#     a=10
#     b=10
# c=A.a+A.b
# print(c)
# # simple interest in class type /static data members
# class A:
#     p=14400
#     r=23   # class type /static data members
#     t=2
# obj=(A.p*A.r*A.t/100)
# print(obj)

# Complete example of Static:-
# class StaticVar:
#     schoolname = "IPS"   #class type
#     def fun():       #class type method
#         a=10  #local class type
#         print(a)
#         print(StaticVar.schoolname)


# print(StaticVar.schoolname)
# StaticVar.fun()

# instance type or dynamic type data members
# class Dynamic :
#     def __init__(self,a,b):
#         self.a = a  # instance type of dynamic variable
#         self.b = b
#     def display(self):
#         print("a",self.a,"b",self.b)
# obj=Dynamic(10,20)
# obj.b=500
# obj.display()

# simple interest using dynamic data members
class SI:
    def fun(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t
        res=(p*r*t)/100
        print(res)
obj=SI()
obj.fun(1200,21,4)



























