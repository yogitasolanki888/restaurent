# Write a Python function to find the Max of three numbers.
def max(x,y):
    if x>y:
         return x
    return y
def maxthree(x,y,z):
    return max(x,max(y,z))

print(maxthree(5,10,12))
