# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
# import json
# x={'4': 5, '6': 7, '1': 3, '2': 4}
# print(x)
# y=json.dumps(x,sort_keys=True , indent=4)
# print(y)

# 5 Write a Python program to convert JSON encoded data into Python objects.
# import json

# dt =  '{"name": "David", "age": 6, "class": "I"}'
# lst =   '["Red", "Green", "Black"]'
# s = '"Python Json"'
# n = '1234'
# f =  '21.34'

# p =  json.loads(dt)
# y = json.loads(lst)
# t =  json.loads(s)
# h =   json.loads(n)






# o = json.loads(f)
# print(p)
# print(y)
# print(t)
# print(h)
# print(o)

# 6. Write a Python program to create a new JSON file from an existing JSON file.
# import json

# with open('states.json',"w+") as f:
#   state_data= json.load(f)

# for state in state_data['states']:
#   del state['area_codes']

# with open('new_states.json', 'w') as f:
#   json.dump(state_data, f, indent=2)


# Check whether an instance is complex or not

# import json

# def encode_complex(object):
#     # check using isinstance method
#     if isinstance(object, complex):
#         return [object.real, object.imag]
#     # raised error if object is not complex
#     raise TypeError(repr(object) + " is not JSON serialized")

# complex_obj = json.dumps(2 + 3J, default=encode_complex)
# print(complex_obj) 


#9.Write a Python program to access only unique key value of a Python object.
# import json
# obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
# print(obj)
# x=json.loads(obj)
# print(x)

# text = input("type in enter")  # or raw_input in python2
# if text == "":
#     print("you pressed enter")
# else:
#     print("you typed some text before pressing enter")

# num=int(input("enter number to convert  "))
# print(human_format(num))
# def human_format(num):
#     decimal_format  = '{:.2f}'
#     # int_num = int(num)
#     if num> 999 and num < 1000000:
#         return decimal_format.format(num/1000.0).rstrip('0').rstrip('.') + 'K' 
#     elif num > 999999:
#         return decimal_format.format(num/1000000.0).rstrip('0').rstrip('.') + 'M'
#     elif num < 1000:
#         return str(num)
# num=int(input("enter number"))
# print(human_format(num))


def convert(num):
   decformat = '{:.1f}'
   if num<1000:
        return (num)
   elif num>999 and num<1000000:
      return decformat.format(num/1000.0).rstrip('0').rstrip('.') + 'K'
   elif num>999999 and num<1000000000:
       return decformat.format(num/1000000.0).rstrip('0').rstrip('.') + 'M'
   elif num>999999999 and num<1000000000000:
       return decformat.format(num/1000000000.0).rstrip('0').rstrip('.') + 'B'
   else:
       return " number above of Trillion "
   
num= int(input("enter number"))
print(convert(num))

