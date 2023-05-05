# json to python using json.loads()
# python to json using json.dumps()


# json to python using loads()
# import  json
# sample= '{ "name1":"Hello,", "name2":"World!"}'
# data = json.loads(sample)
# print(data)
# print(f' {data["name1"]} {data["name2"]}')
# print(f'{data["name1"]} {data["name2"]}')

# python to json conversion using dumps()
# import  json
# a=(1,"c",2,"d",3,"d")
# y=json.dumps(a)
# y=json.dumps(a,indent=4 , separators=(","," = "))
# print(y)
# print(type(y))
# print(type(a))


# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# y=json.dumps(x)
# print(y)
# y=json.dumps(x, indent=4, sort_keys= True)
# print(y)
# print(type(y))

# data={
#     "records": {
#         "2": {
#             "id": 2,
#             "first_name": "rahul",
#             "middle_name": "singh",
#             "last_name": "thakur",
#             "date": "2023-03-17 13:32:29.673060"
#         },

#     }
# }
data= {
    "records": {
        "2": {
            "id": 2,
            "first_name": "rahul",
            "middle_name": "singh",
            "last_name": "thakur",
            "date": "2023-03-17 13:32:29.673060"
            
        },
        "4": {
            "id": 4,
            "first_name": "divya",
            "middle_name": "kumari",
            "last_name": "solanki",
            "date": "2023-03-17 13:35:59.282433"
        },
        "7": {
            "id": 7,
            "first_name": "neha ",
            "middle_name": "singh",
            "last_name": "rajput",
            "date": "2023-03-17 16:34:37.177271"
        },
        "8": {
            "id": 8,
            "first_name": "sawan",
            "middle_name": "na",
            "last_name": "jadhav",
            "date": "2023-03-17 16:57:44.301932"
        },
        "10": {
            "id": 10,
            "first_name": "rohit",
            "middle_name": "singh ",
            "last_name": "sharma",
            "date": "2023-03-17 17:04:59.260339"
        },
        "11": {
            "id": 11,
            "first_name": "rishabh",
            "middle_name": "kumar",
            "last_name": "pant",
            "date": "2023-03-17 17:06:18.255576"
        }
    },
    "meta": {
        "last_id": "11"
    }
}

# add_key= input("enter key ")
# add_val=input("enter value ")
# for i in data["records"]:
#         for key in i:
#             data["records"][key]["city"]="indore"
#             # [key]add_key=add_val
# print(data)
for key in data["records"].keys():
    data["records"][key]['Seen'] = False
print(data)