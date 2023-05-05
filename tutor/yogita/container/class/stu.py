# wap to manage student record roll, marks,age
class Student:
    def accept(self,rollno,marks,age):
        self.rollno = rollno
        self.marks =marks
        self.age = age
    def display(self):
        print("roll no :"+ str(self.rollno) + " marks :"+ str(self.marks) + "age :"+ str(self.age))
obj=[]
for i in range(0,2):
    o=Student()
    o.accept(int(input("enter rollno:")),int(input("enter marks:")),int(input("enter age:")))
    obj.append(o)
print(len(obj))
m=0
for i in range(0,2):
    if m<obj[i].marks:
        m=obj[i].marks
print("max marks",m)
    # obj[i].display()1

list

# class Student:
#     def accept(self,rno,marks,age):
#         self.rno=rno
#         self.marks=marks
#         self.age=age

#     def display(self):
#         print("rno is "+str(self.rno) + "marks is "+str(self.marks) + "age is "+str(self.age))



# obj = []

# for i in range(0,2):
#      o= Student()
#      o.accept(int(input("Enter rno")),int(input("Enter marks")),int(input("Enter Age")))
#      obj.append(o)

# print(len(obj))
# mx=0
              
# for i in range(0,2):
#        if mx<obj[i].marks:
#               mx = obj[i].marks
# else:
#     print("Maximum mark is ",mx)
