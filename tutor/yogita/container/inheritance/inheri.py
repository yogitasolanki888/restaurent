# expl1 inheritance
#Program to Manage Companyname and Manager
# class Company:
#     def accept(self,name):
#         self.name=name
#     def display(self):
#         print("company name: " + self.name)
# class Manager(Company):
#     def accept1(self,eid,ename):
#         self.eid=eid
#         self.ename=ename
#     def display1(self):
#         print("eid is ", self.eid,"name is ", self.ename)
# obj = Company()
# obj.accept("xyz")
# obj.display()
# obj1 = Manager()
# obj1.accept("xyz")
# obj1.accept1(1001,"ABC")
# obj1.display()
# obj1.display1()

# another exple
# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def display(self):
#         print(self.fname,self.lname)
# class Child(Person):
#         pass
# obj=Person("yogita","solanki")
# obj.display()
 
 # create  init method in child class in call to parent class init method
 # another exple
# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def display(self):
#         print(self.fname,self.lname)
# class Child(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
# obj=Child("yogita","solanki")
# obj.display()

# call parent class using super() method 
# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def display(self):
#         print(self.fname,self.lname)
# class Child(Person):
#     def __init__(self,fname,lname,year): # add year parameter
#         super().__init__(fname,lname)
#         self.passingyear= year  # add properties
# obj=Child("neha","sharama",2021)
# obj.display()
# print(obj.passingyear)

# add methods in child class
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(self.fname,self.lname)
class Child(Person):
    def __init__(self,fname,lname,year): # add year parameter
        super().__init__(fname,lname)
        self.passingyear= year  # add properties
    def Welcome(self):
        print("Welcome",self.fname,self.lname,"to the ",self.passingyear)
obj=Child("neha","sharama",2021)
# obj.display()
# print(obj.passingyear)
obj.Welcome()
