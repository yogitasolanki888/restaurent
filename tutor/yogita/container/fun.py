# def function(fname, lname):
# print(fname + " " + lname)


# function("yogita", "solanki")


# def func(*kids):
# print("the youngest child is :" + kids[1])


# func("neha", "abc", "zxc")


# def my_function(child3, child2, child1):
#    print("The youngest child is " + child2,child1)


# my_function(child2="Emil", child3="Tobias", child1="Linus")

# def keyword(**kids):
# print("the youngest child is " +kids["lname"])

# keyword(fname="xy",lname="sharama",f1name="neha")


# default function


def my_function(city="indore"):
    print("the city is " + city)


my_function("bhopal")
my_function()
my_function("riva")


def func(food):
    for x in food:
        print(x)
lst = ["apple", "banana", "orange", "charry"]
func(lst)

# return value
def func(x,y):
    return x *y

print(func(5,20))
print(func(1,2))