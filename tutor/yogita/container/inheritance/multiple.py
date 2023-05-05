# multiple inheritance  two base classes in one child class
# class A:
#      methods

# class B:
#     methods

# class C(A, B):
#     methods

# example
# class base1:
#     def addition(self,a,b):
#         return a + b
# class base2:
#     def multiplication(self, a,b):
#         return a * b
# class derived(base1,base2):
#     def division(self, a,b):
#         return a / b
# obj=derived()
# print(obj.addition(10,20))
# print(obj.multiplication(20,40))
# print(obj.division(5,2))

# another example
class Company:
    def fun(self):
        print("company information")
    def accept(self, cname):
        self.cname = cname
    def display(self):
        print("company name",self.cname)
class Manager:
    def accept1(self,mid,mname):
        self.mid=mid
        self.mname=mname
    def display1(self):
        print("manager id",self.mid,"manager ",self.mname)
class Employee(Company,Manager):
    
    def accept2(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def display2(self):
        print("employee id ",self.eid,"employee  ",self.ename)

obj1=Employee()
obj1.fun()
obj1.accept("mnc")
obj1.accept1(1002,"john")
obj1.accept2(1002,"mike")
obj1.display()
obj1.display1()
obj1.display2()


