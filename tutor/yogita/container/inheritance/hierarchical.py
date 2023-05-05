# heirarchical inheritance  One base class to different child class
# class A:
#    methods

# class B(A):
#    methods

# class C(A):
#     methods

# class Parent:
#     def fun1():
#         print("this is base class ")
# class Child1(Parent):
#     def fun2():
#         print("this is child class")
# class Child2(Parent):
#     def fun3():
#         print("this is child2 class ")
# obj=Child1
# obj1=Child2
# obj.fun1()
# obj.fun2()
# obj1.fun1()
# obj1.fun3()

# class Company:
#     def accept(self,cname):
#         self.cname=cname
#     def display(self):
#         print("name of company",self.cname)
# class Manager(Company):
#     def accept1(self,mid,mname):
#         self.mid=mid
#         self.mname=mname
#     def display1(self):
#         print("manager id",self.mid,"name",self.mname)
# class Employee(Company):
#     def accept2(self,eid,ename,esal):
#         self.eid=eid
#         self.ename=ename
#         self.esal=esal
#     def display2(self):
#         print("employee id",self.eid,"name",self.ename,"salary",self.esal)
# obj1=Manager()
# obj1.accept("mnc")
# obj1.accept1(100,"john")
# obj1.display()
# obj1.display1()

# obj2=Employee()
# # obj2.accept("xyz")
# obj2.accept2(1002,"mike",15000)
# # obj2.display()
# obj2.display

# MRO example

class A:
    def method(self):
        print("A.methhod is called")
class B:
    pass

class C(A,B):
    pass

class D(C,B): # class D(B,C): # error 
    pass

x=D()
x.method()



