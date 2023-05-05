# try:
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("demonitator can not be zero")
# except ValueError:
#     print("enter only numerical values")
# print("line1")
# print("line2")

# try:
#     f=open("demo.txt")
#     try:
#         f.write("hello exception handling")
#     except:
#         print("semthonig went wrong when writing the file")
#     finally:
#         f.close()
# except:
#     print("something went wrong when opening file")

#finally
# try:
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("demonitator can not be zero")
# except ValueError:
#     print("enter only numerical values")
# finally:
#     print("execute finally block")  # finally block by default execute hota h 

# Example of Try..except--else --finally
# try:
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("demonitator can not be zero")
# except ValueError:
#     print("enter only numerical values")
# else:
#     print("not found  any errors")
# finally:
#     print("finally block execute")
# print("line1")
# print("line2")

# count=0
# flag = True
# while(flag):
#     try:
#       a=int(input("enter first number"))
#       b=int(input("enter second number"))
#       c=a/b
#       print(c)
#     except Exception:
#        print("demonitator can not  be zero")
#     else:
#        flag=False
#     finally:
#         count=count+1
#         print("no. of attempt"+str(count))


# Complete Example of Exception:-

# c=0
# s=''
# try:
#  a= int(input("enter first number"))
#  b= int(input("enter second number"))
#  c=a/b
 
# except ZeroDivisionError:
#     s = 'Result is default'
#     print("denominator can not be zero")

# except ValueError:
#     s='Result is default'
#     print("Enter only numeric value")
# else:
#     s="Result is Accurate "

# finally: 
#    print(s,c)

# i = 1
# try:
#     i.append(2)
# except AttributeError:
#     print('No such attribute')

# try:
#      string = input()
#      print(string)
# except EOFError:
#      print("no data provided to input function")
class SalaryException(Exception):
    pass

try:
    sal=int(input("enter salary"))
    if sal<10000:
        raise SalaryException
    else:
        print("salary is " + str(sal))

except SalaryException:
    print("salary should be above 10000")































