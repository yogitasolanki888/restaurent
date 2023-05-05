# "w+" write/read 
# "r+" read/write
# "a+" append/read
# write() write contents info  of file 
# read() read content
#append() append contents info of file
# 4 append file:

# f = open("student.txt","a")
# s = input("write content")
# f.write(s)

# f.close()

import time
# f = open("expenses.txt","w")
# expenseby = input("Enter expense by")
# grocerry = input("Enter grocerry details")
# milk = input("Enter milk expenses")
# rent = input("Enter rent expenses")
# date = time.asctime(time.localtime(time.time()))
# f.write("Today Expenses Details")
# f.write("\n")
# f.write("Grocerry:"+grocerry)
# f.write("\n")
# f.write("Milk:" +milk)
# f.write("\n")
# f.write("Rent:" +rent)
# f.write("\n")
# f.write("Date:" + date)
# f.close()

# append content to the file 
# f=open("expenses.txt","a")
# expenseby = input("Expenses by: ")
# grocerry = input("grocerry details : ")
# milk = input("milk expenses : ")
# roomrent = input("Roomrent expense")
# bill = input("Bill expense")
# date =time.asctime(time.localtime(time.time()))
# f.write("\n")
# f.write("expenses by "+ expenseby)
# f.write("\n")
# f.write("grocerry details"+grocerry)
# f.write("\n")
# f.write("milk "+milk)
# f.write("\n")
# f.write("roomrent "+roomrent)
# f.write("\n")
# f.write("bijali bill "+bill)
# f.write("\n")
# f.write("Date: "+date)
# f.close()

# open file w+ mode write/read
# f=open("expenses.txt","w+")
# expenseby = input("Expenses by: ")
# grocerry = input("grocerry details : ")
# milk = input("milk expenses : ")
# roomrent = input("Roomrent expense")
# bill = input("Bill expense")
# date =time.asctime(time.localtime(time.time()))
# f.write("\n")
# f.write("expenses by "+ expenseby)
# f.write("\n")
# f.write("grocerry details"+grocerry)
# f.write("\n")
# f.write("milk "+milk)
# f.write("\n")
# f.write("roomrent "+roomrent)
# f.write("\n")
# f.write("bijali bill "+bill)
# f.write("\n")
# f.write("Date: "+date)
# f.seek(0)
# s=f.read()
# print(s)
# f.close()

# open file "a+" mode append/read 
# f=open("expenses.txt","a+")
# expenseby = input("Expenses by: ")
# grocerry = input("grocerry details : ")
# milk = input("milk expenses : ")
# roomrent = input("Roomrent expense")
# bill = input("Bill expense")
# date =time.asctime(time.localtime(time.time()))
# f.write("\n")
# f.write("expenses by "+ expenseby)
# f.write("\n")
# f.write("grocerry details"+grocerry)
# f.write("\n")
# f.write("milk "+milk)
# f.write("\n")
# f.write("roomrent "+roomrent)
# f.write("\n")
# f.write("bijali bill "+bill)
# f.write("\n")
# f.write("Date: "+date)
# f.seek(0)
# s=f.read()
# print(s)
# f.close()

class FileOperation:
    def createFile(self):
       self.f = open("info.txt","a+")
    def writeFile(self):
      title = input("Enter title")
      self.f.write("\n"+title)
      desc = input("Write content")
      self.f.write("\n"+desc)
    def readFile(self):
      self.f.seek(0)  #it will reset cursor position to any index
      res = self.f.read()
      print(res)
      self.f.close()

obj = FileOperation()
obj.createFile()
obj.writeFile()
obj.readFile()













  