# def calculate(a, b):
#     mean = (a * b) / (a + b)
#     print(mean)
# a = 8
# b = 9

# calculate(a, b)


# ## default argument
# def average(a=9, b=3):
#     print("average", (a + b) / 2)


# average(b=5)


# def name(name,fname="amy", lname="jain"):
#     print("hello", name, fname, lname)

# name("yogi", "sara","xyz")

# # keyword arguments
# def average(a=9, b=3):
#     print("average", (a + b) / 2)


# average(b=5,a=2)

# #
# # required arguments
# def average(a, b, c=3):
#     print("average", (a + b+c) / 2)
# average(3,4)


## variable length arguments
# def average(*numbers):
#     s = 0
#     for i in numbers:
#         sum = s + i
#     print("average", (sum / len(numbers)))


# average(3, 4, 4, 6)

def name(**name):
    print(type(name))
    print("hello", name["fname"],name["mname"],name["lname"])

name(fname="yogi", lname="sara",mname="xyz")