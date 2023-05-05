lst= ['gfg',8,'is',3]
key= ["name", "id"]
final = {}
for i in range(len(lst)):
    final[key[i]]=lst[i]
print(final)