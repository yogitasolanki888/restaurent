# multilevel inheritance from base class to derived class and derived class to sub derived class
#exple
# class A:
    # methods
# class B(A):
    # methods
# class C(B):
    # methods

# class A:
#     def fun(self):
#         print(" hello class A")
# class B(A):
#     def fun1(self):
#         A.fun(self)
#         print(" hello class B")
# class C(B):
#     def fun2(self):
#         B.fun1(self)
#         print(" hello class C")
# obj=C()
# obj.fun2()

# another example
# class Company:
#     def accept (self):
#         self.cname = "abc"
#     def display (self):
#         print("company name is " + str(self.cname))
# class Manager(Company):
#     def accept1(self):
#         self.eid="111"
#         self.ename="john"
#         # super().accept(self)
#     def display1(self):
#         print("eid is " + str(self.eid), "ename is " + str(self.ename))
# class Developer(Manager):
#     def accept2(self):
#         self.sal=15000
#         # super().accept1(self)
#     def display2(self):
#         print("salary: " + str(self.sal))
        
# obj1 = Manager()
# obj1.accept()
# obj1.accept1()
# obj1.display()
# obj1.display1()

# obj2 = Developer()
# obj2.accept()
# obj2.accept1()
# obj2.accept2()
# obj2.display()
# obj2.display1()
# obj2.display2()

class Company:
    def __init__(self ):
        self.cid= 101
        self.cname= "mnc"
    def display(self):
        print("Company id ",self.cid,"Company name ",self.cname)
class Manager(Company):
    def __init__(self):
        self.mid= 102
        self.mname= "john"
        Company.__init__(self)
    def display1(self):
        print("Manager id ",self.mid,"Manager name ",self.mname)
class  Employee(Manager):
    def __init__(self):
        self.eid= 103
        self.ename="mike"
        Manager.__init__(self)
    def display2(self):
        print("Employee id ",self.eid,"Employee name ",self.ename)
obj=Employee()
obj.display()
obj.display1()
obj.display2()


        
      