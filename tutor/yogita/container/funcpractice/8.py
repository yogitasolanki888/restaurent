# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(list):
    b=[]
    for i in list:
        if i not in b:
            b.append(i)
    return b

l=[1,2,3,3,3,3,4,5]
print(unique_list(l))