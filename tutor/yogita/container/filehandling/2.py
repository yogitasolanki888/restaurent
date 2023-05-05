#5. Write a Python program to read a file line by line and store it into a list. 
# def read_file(filename):
#     f=open(filename,"r")
#     list=f.readlines()
#     print (list)
# read_file("just.txt")

#6.Write a Python program to read a file line by line store it into a variable.
# def readlinebyline(fname):
#     f=open(fname,"r")
#     a=f.readlines()
#     print (a)
# readlinebyline("just.txt")

# 7.Write a Python program to read a file line by line store it into an array.
# def readfile(fname):
#     l=[]
#     f=open(fname,"r")
#     for x in f:
#         l.append(x)
#     print(l)
# readfile("just.txt")

#8.Write a python program to find the longest words.
# def longest_word(fname):
#     f=open(fname,"r")
#     b=f.read().split()
#     # print(b)
#     maxlen=(len(max(b,key=len)))
#     for x in b:
#         if len(x)==maxlen:
#             print(x)
# longest_word("just.txt")

#9.Write a Python program to count the number of lines in a text file.
# def count_lines(fname):
#     c=0  
#     f=open(fname,"r")
#     for x in f: 
#         c=c+x.count(x)
#     print (c) 
# count_lines("just.txt")

# 10. Write a Python program to count the frequency of words in a file.
# def frequency_count(fname):
#     d={}
#     f=open(fname,"r")
#     s= f.read().split()
#     # print(s)
#     for x in s:
#         if x in d:
#            d[x]=d[x]+1
#         else:
#             d[x]=1
#     print(d)
# frequency_count("just.txt")

# s="  welcome"
# print(s.strip())
# s1="hellowrold"
# s=[]
# for i in s1:
#    s.append(i.strip())
# print(s)

# Write a Python program to write a list content to a file.
# def write_list(fname):
#     f=open(fname,"w+")
#     a=input("enter item ")
#     f.write(a)
#     print(f.read())
# write_list("just.txt")

# def write_list(fname):
#     c= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#     f=open(fname,"w+")
#     for x in c:
#        f.write("\n")
#        f.write(x)
#     f=open(fname,"r")
#     print(f.read())

# write_list("just.txt")








