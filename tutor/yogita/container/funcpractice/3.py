# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def mul(num):
    m=1
    for i in num:
       m=m*i
    return m

x=[8, 2, 3, -1, 7]
print(mul(x))

