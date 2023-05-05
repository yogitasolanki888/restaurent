# Enter first number:
# Enter second number:
# Select operation:
# 1. +
# 2. -
# 3. *
# 4. /
# 5. Exit
# Output print
def calculate():
    global a,b
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
def add():
    c=a+b
    print(c)
def sub():
    c=a-b
    print(c)
def mul():
    c=a*b
    print(c) 
def div():
    c=a/b
    print(c) 
def operations():
    while (True):
        ope=input("enter 1 for add" "\n" "enter 2 for subtract" "\n" "enter 3 for multiplication" "\n" "enter 4 for division")
        if ope=="1":
            calculate()
            add()
        elif ope=="2":
            calculate()
            sub()
        elif ope=="3":
            calculate()
            mul()
        elif ope=="4":
            calculate()
            div()
        else:
            pass
operations()




