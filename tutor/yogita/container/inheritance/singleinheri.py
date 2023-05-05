# example of single inheritance
# class Company:
#     def accept(self):
#         self.cid =1001
#         self.cname="abcd"
#     def display(self):
#         print("company cid: ", self.cid)
#         print("company cname: ", self.cname)
# class Manager(Company):
#     def accept1(self,sal):
#         self.sal = sal
#     def display1(self):
#         print("sal: ", self.sal)
# obj=Manager()
# obj.accept()
# obj.display()
# obj.accept1(15000)
# obj.display1()

# another way using init method 
class Company:
    def __init__(self):
        self.cid=101
        self.cname="abc"
    # def display(self):
    #     print("Company cid: " + str(self.cid))
    #     print("Company name: " + str(self.cname))
class Manager(Company):
    def __init__(self,sal):
        Company.__init__(self)
        self.sal=sal
    def display1(self):
        print("company id: " + str(self.cid),"cname: " + str(self.cname),"sal: " + str(self.sal))
obj=Manager(15000)
obj.display1()
