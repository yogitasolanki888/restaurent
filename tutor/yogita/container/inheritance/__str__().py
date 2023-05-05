# __str__() method  class using print()
# without str method return the <__main__.A object at 0x0000013994AE6D50>
# class A:
#     def __init__(self,name,address):
#         self.name= name
#         self.address= address
# obj=A("xyz","fghjkl")
# print(obj) # 

# class A:
#     def __init__(self,fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#     def __str__(self):
#         return f"{self.fname} {self.lname} {self.age}"
# obj =A("yogi","solanki",21)
# print(obj)

# without __str__() and __repr__()
# class Employee:
#     def __init__(self,eid,ename,esalary):
#         self.eid = eid
#         self.ename =ename
#         self.esalary = esalary
# obj=Employee(12,"abc", 1500)
# print(str(obj))
# print(repr(obj))

# class Employee:
#     def __init__(self,eid,ename,esalary):
#         self.eid = eid
#         self.ename =ename
#         self.esalary = esalary
#     def __str__(self):
#         return f"eid is {self.eid} ename is {self.ename} esalary is {self.esalary}"
#     def __repr__(self):
#         return f" {self.eid} {self.ename} {self.esalary}"
# obj=Employee(12,"abc", 1500)
# print(obj)
# print(repr(obj))

import datetime
today= datetime.datetime.now()
print(str(today))
print(repr(today))






