# class Myclass:
#     x=10
# p1=Myclass()
# print(p1.x)
#exple
# class MyClass:
#     id=10
#     name="yogita"
#     def displaye(self): # displaye the information
#         print(self.id,self.name)
# a=MyClass()
# a.displaye()

#delete class object
# class MyClass:
#     id=10
#     name="yogita"
#     def displaye(self): # displaye the information
#         print(self.id,self.name)
# a=MyClass()
# del a.id
# del a
# a.displaye()
  
# expl2
# class Student:
#     def accept(self):
#         self.rolno=input("enter roll no.")
#         self.sname=input("enter name")
#     def display(self):
#          print("roll no.",self.rolno,"name of student",self.sname)

# obj=Student()
# obj.accept()
# obj.display()
# for i in range(5):
#     obj1=Student()
#     obj1.accept()
#     obj1.display()

# expl3
# class Student:
#     def accept(self,rollno,sname):
#         self.rollno=rollno
#         self.sname=sname
#     def display(self):
#         print("rollno. is ", self.rollno,"name is ", self.sname)

# obj=Student()
# obj.accept("100","yogita")
# obj.display()

# for i in range(5):
#     obj.accept("200","neha")
#     obj.display()

# another example of class and object
# from distutils.log import info


# class Example:
#     def info(self,id,name,job,salary):
#         self.id =id
#         self.name=name
#         self.job=job
#         self.salary=salary
#     def display(self):
#         print("id",self.id)
#         print("name" , self.name)
#         print("job ", self.job)
#         print("salary" , self.salary)
# obj=Example()
# obj.info(100,"yogita","intern","2000")
# obj.display()


# class Example:
#     def accept(self,id,name,job,salary):
#         self.id =id
#         self.name=name
#         self.job=job
#         self.salary=salary
#     def display(self):
#         print(" id " + str(self.id)+ " name "+ str(self.name)+ " job "+ str (self.job) + " salary " + str (self.salary))
        
# obj=Example()
# obj.info(100,"yogita","intern","2000")
# obj.display()

# item=int(input("enter number of students"))
# obj=[]
# for i in range(item):
#     o=Example()
#     o.accept(int(input("enter id")),input("enter name"),input("enter job"),int(input("enter salary")))
#     obj.append(o)
# for i in range(item):
#     obj[i].display()

# components of class
#1 data members and variables
   #a class type or static 
   #b instance type or dynamic
#2 member function or function
  #a class type or static 
  #b instance type or dynamic 

class SI:
    def accept(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t

    def logic(self):
        self.si = (self.p*self.r*self.t)/100

    def display(self):
        print("Result is ",self.si)

obj = SI()
p = float(input("Enter amount"))
r = float(input("Enter rate"))
t = float(input("Enter time"))
obj.accept(p,r,t)
obj.logic()
obj.display()

