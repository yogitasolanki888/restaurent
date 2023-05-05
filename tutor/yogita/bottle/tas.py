# a="12232"
# # num=int(input("enter number"))
# b=[]
# # for  i in a:
# for j in range(0,len(a)):
#      b.append(a.replace(a[j],""))
# print(b)
# print(max(b))


# a=12232

 
# s = ' \n a b c \t'
# s="aabc abc bbccaa"
# print(s.rstrip("abc"))


# a=["slice","banana","cherry","cheese","banana","apple","orange"]
# for item in a:
#     if item=="banana" :
#         a.remove(item)
# print(a)
# b=[]
# s1=""
# s="12232"
# # for i in range(0,len(s)):
# #     if i==i:
# #         s1=s1+s[i]
# #         b.append(s1)
# # print(b)

def remove_char(s,s1):
    new=""
    for i in range(0,len(s)):
        # if i!=s1:
        new=new+s[i]
    return new
s=input("enter a string:-")
s1=int(input("Enter a ith char to remove: "))
print(remove_char(s,s1))