# "r"= read ,error if file not exists
# "w"= write ,create file if not exists / override
# "a" = append ,create file if not exists
# "x" = create file 
# "t" = text mode
# "b" =binary mode like image

# create file new file 
# f = open("welcome.txt", "x")

# create and write
# f=open("demo.txt","w")
# f.write("hello world  gjk jdkl shjskldk sjklds ssddhjaskl sjkl \n dfg safghj agjkls sghajs aghsjsa ghjas ghjd ghjkl\n sdfg sdquiowo wiopwd ghdhksjdlk nbsd dfghjkl")
# f.close()

# readfile 
# f= open("demo.txt","r")
# print(f.read(10))
# print(f.readline())
# print(f.readline())
# f.close()

 # by looping read a file 
# f = open("demo.txt","r")
# for x in f:
#     print(x)
# f.close()

# append 
# f = open("demo.txt","a")
# f.write(" welcome to the new file ..\n jhkfj sghjsdk gjksla ghjkls \n sdfghjk fgjknz ghjklds ghjdklas To write to an existing file,\n  you must add a parameter to the ")
# f.close()
# f =open("demo.txt","r")
# print(f.read())
# f.close()

# w overwrite the entire file
# f = open("demo.txt","w")
# f.write("opps! overwrite this file  and deleted previous data")
# f.close()
 
# f = open("demo.txt","r")
# print(f.read())


# "x" - Create - will create a file, returns an error if the file exist
# f = open("myfile.txt", "x")

#"a" - Append - will create a file if the specified file does not exist
# f = open("myfile.txt", "a")

# "w" - Write - will create a file if the specified file does not exist
# f = open("myfile.txt", "w") 







































































# remove file 
# import os
# if os.path.exists("welcome.txt"): # check file if exists 
#   os.remove("welcome.txt") # remove
# else:
#   print("The file does not exist")

# # delete entire folder using rmdir()
# import os
# os.rmdir("myfolder")

# open file with with()
# with open("student.txt","w+") as f:
#     f.write("ggh vbn hj gh gh ")
#     a=f.read()
#     print(a)

#  split() function
# Python code to illustrate split() function
# with open("just.txt", "r") as f:
# 	data = f.readline()
# 	for x in data:
# 		word = x.lstrip()
# 		print (word)
		

# seek() method  
# f=open("just.txt", "r")
# #Moving the file handle to 6th character 
# f.seek(6)
# s=f.read()
# print(s)

# seek() pass the offset and whence and write the content end of the file 
f=open("just.txt","r+")
f.seek(0,2)
f.write("\n this is end of the file ")
f.seek(0)
print(f.read())



 
