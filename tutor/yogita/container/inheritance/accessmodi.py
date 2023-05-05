# access modifier
# 1 public ,outside the class
# 2 protected , outside the class in derived and  sub child classes (_)
# 3 private , only class (_ _)

# example public
# class Employee:
#     def __init__(self,ename,esal):
#         self.ename =ename
#         self.esal=esal
# obj= Employee("abc",15000)
# print(obj.esal)  # public

# protected
# class Employee:
#     def __init__(self,ename,esal):
#         self._ename =ename # protected attribute
#         self._esal = esal  # protected attribute
# class Hr(Employee):
#     def task(self):
#         print("we are managing")
# obj= Employee("abc",16000)
# print(obj._esal) # protected

# obj1=Hr("xyz",34567)
# print(obj1._esal)
# obj1.task()

# private
# class Employee:
#    def __init__(self,name,sal):
#     self.__name = name
#     self.__sal = sal
# e= Employee("sofy",56789)
# print(e.__sal) # get a error


# class Company:
#     def __init__(self):
#         self.name = "Mnc"
#         self._proj = "abc"

#     def show(self):
#         print("show data of company")


# class Employee(Company):
#     def __init__(self, ename, esal):
#         Company.__init__(self)
#         self._ename = ename
#         self.__esal = esal

#     def showdata(self):
#         print("employee name: ", self._ename, "salary: ", self.__esal)


# obj = Employee("vbbn", 56770)
# print(obj._ename)
# import pdb

# pdb.set_trace()
# print(obj._Employee__esal)
# obj.showdata()
# obj.show()


# name mangling 

# class Company:
#     p=67
#     _prot=789
#     __private=678
# obj = Company()
# print(obj.p)
# print(obj._prot)
# import pdb

# pdb.set_trace()
# print(obj._Company__private) # name mangling

class Student:
    def __init__(self,sname,srole,sbranch):
        self._sname = sname
        self.__srole = srole
        self.__sbranch = sbranch
    def show (self):
        print(f" {self._sname},{self.__srole} ,{self.__sbranch} ")
        
class College(Student):
    def __init__(self,sname,srole,sbranch ,cname,cadd):
        Student.__init__(self,sname,srole,sbranch )
        self._cname = cname
        self._cadd = cadd

    def showStudentdata(self):
        print(self._cname)
        print(self._cadd)
        # self.show()
obj=College("yogita",121,"cse","piemr","vijay nagar")
# import pdb

# pdb.set_trace()
obj.showStudentdata()
# obj.show()
# print(obj._sbranch)
print(Student.__dict__)

