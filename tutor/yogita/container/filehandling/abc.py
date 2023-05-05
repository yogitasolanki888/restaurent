# with open("just.txt","rb") as f:
#     f.seek(3)
#     print(f.read(5).decode("utf-8"))
#     f.seek(10,1)
#     print(f.read(6).decode("utf-8"))

# tell() Function To Get File Handle Position
# open file for reading and writing  r+
# with open(r'student.txt', "r+") as f:
#     # Moving the file handle to the end of the file
#     f.seek(0, 2)

#     # getting the file handle position
#     print('file handle at:', f.tell())

#     # writing new content
#     f.write("\nDemonstrating tell")

#     # getting the file handle position
#     print('file handle at:', f.tell())

#     # move to the beginning
#     f.seek(0)
#     # getting the file handle position
#     print('file handle at:', f.tell())

#     # read entire file
#     print('***Printing File Content***')
#     print(f.read())
#     print('***Done***')

#     # getting the file handle position
#     # print('file handle at:', f.tell())

# file handle at: 17
# file handle at: 37
# file handle at: 0
# ***Printing File Content***
# ggh vbn hj gh gh 
# Demonstrating tell
# ***Done***
# file handle at: 37

# rename() to rename a file name
import os
# old="just.txt"
# new= "new_just.txt"
# os.rename(old,new)
# os.remove("info.txt")
#

#os.path.isfile
old="new_just.txt"
new= "just.txt"
if os.path.isfile(new):
    print("file already exists")
else:
    os.rename(old,new)


