# class FactorialError(Exception): pass


# def factorial(n):

#     if n < 0:
#         raise FactorialError('Factorial expects non-negative integers')
#     return 1 if n == 0 else n*factorial(n-1)

# n=int(input("enter number to clculte factorial"))
# print(factorial(n))

def Division(a,b):
    try :
        return a/b 
    except ZeroDivisionError:
        print("demonitator not be zero")
a= int(input("enter first number"))
b= int(input("enter second number"))
print(Division(a,b))

# Question 2: Perfect division function with clean-up action
