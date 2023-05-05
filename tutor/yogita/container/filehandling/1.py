# Write a Python program to read an entire text file.
# def file_read(fname):
#         txt = open(fname)
#         print(txt.read())

# file_read('just.txt')


# def fileread(fname):
#         f=open(fname)
#         print(f.read())
# fileread("just.txt")

# Write a Python program to read first n lines of a file.
# def read(fname,n):
#         f=open(fname,"r")
#         # f.seek(0)
#         # print(f.read())
#         for x in (f.readlines()[:n]):
#              print(x,end="")
# n=4
# read("just.txt",n)

# 3.Write a Python program to append text to a file and display the text. 
# def app_write():
#     f=open("just.txt" ,"w+")
#     a=input("enter content of file ")
#     f.write(a)
#     f.seek(0)
#     print(f.read())
#     f.close()
# app_write()

#4.Write a Python program to read last n lines of a file.
# def read_last_line(fname,n):
#     f=open(fname,"r")
#     for x in (f.readlines()[-n:]):
#         print(x,end=" ")
# n=4
# read_last_line("just.txt",n)




    
