# Write a Python function to calculate the factorial of a number . The function accepts the number as an argument
def factorial(num):
    if num==0:
        return 1
    else:
        return num*(num-1)
    # fact=1
    # for i in range(1,num+1):
    #     fact=fact*i
    #     print(str(i),"*",fact)

    
num=int(input("enter the number"))
factorial(num)