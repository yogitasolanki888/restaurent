# main_string = "Dani likes apple, Dani also likes apple"
# query_string = "lik"  # input("input query string")
# occurence = 1  # input("input occurrences")
# output = "Dani kiles apple, Dani also likes apple"

# ans 1

m = "Dani likes apple, Dani also likes apple"
s=m.split()
print(s)
s1 = input("input query string")
rep=s1[::-1]
c = int(input("input occurrence"))
if s1 not in s:
   print(m)
else:
    y=m.replace(s1,rep,c)
    print(y)

# ans 2

# m = "Dani likes apple, Dani also likes apple"
# s1 = input("input query string")
# re=s1[::-1]
# c = int(input("input occurrence"))
# if s1 not in m:
#     print(m)
# else:
    #  x=s1.join(m.split(s1)[:c]) + re + s1.join(m.split(s1)[c:])
#      print(x)
         

# ans 3

# m = "Dani likes apple, Dani also likes apple"
# s1 = input("input query string")
# c = int(input("input occurrence"))
# re=s1[::-1]
# s=list(m)
# b=[]
# for i in s1.split():
#     # print(i)
#     if(s.count(i)>= c):
#         count=0
#         for j in m.split():
#                 print(j)
                # if(i == s[j]):
                #     count+= 1
                #     if(count == c):
                #          b.append(j)
                #     else:
                #          if count==0:
                #                break

# print(b)
# for l in b:
#     s[l] = re
# print("".join(s))
     



        