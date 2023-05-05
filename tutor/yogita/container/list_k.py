# x = [[1, 2, 3, [5, 6, [7, 8, [9], [5, [6]]]], "dtr", [4, ["dt", [56, 67]]]]]

# y = {"name": [1, (2, 3, 5), {"name": [23, {"age": "indore"}]}]}


# y["name"][2]["name"][1]["age"][3]
# [1, 2, {"name": [23, {"age": 11}]}]
# {"name": [23, {"age": 11}]}
# [23, {"age": 11}]
# {"age": 11}
# indore
# o


# nums = [1, 2]


# def sum_of_list(num):
#     return sum(num)


# def get_pow(num, pow):
#     xl = []
#     for i in num:
#         xl.append(i**pow)
#     return sum_of_list(xl)


# flat_num = sum_of_list(nums)
# squared_num = get_pow(nums, 2)
# cubes_num = get_pow(nums, 3)

# print(flat_num + squared_num + cubes_num)

# format method  using {}
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

# using  indexing
# price=47
# itemno = 267
# txt="the price is {0} and the item number is {1}"
# print(txt.format(price, itemno))

name="john"
age = 36
txt="the price is {0} .{0} age is {1}"
print(txt.format(name, age))



#using named indexed
# myorder = "i have a {bikename}  and price of {price}"
# print(myorder.format(bikename="herohonda",price=100000))