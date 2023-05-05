import json
import pdb
import time

# # read file
with open("example.json", "r") as myfile:
    data = myfile.read()
data = json.loads(data)

# print("____________________________________________________________")
# print("    |\t    ".join(data.keys()),"  |  ")
# print("_____________________________________________________________")
print(
    "________________________________________________________________________________________________"
)
# print("{:<15} {:<15} {:<15} {:<15}".format(*data.keys()))
print(
    "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Sno.", "fname", "mname", "lname", "date"
    )
)
print(
    "________________________________________________________________________________________________"
)

# print each data item.
for i in range(data["fname"].__len__()):
    print(
        "{:<15} {:<15} {:<15} {:<15} {:<15}".format(
            i+1, data["fname"][i], data["mname"][i], data["lname"][i], data["date"][i]
        )
    )
    print(
        "________________________________________________________________________________________________"
    )


# print("____________________________________________________________")
# print("  |\t    ".join(data.keys()),"|")
# print("_____________________________________________________________")

# for i in range(data["fname"].__len__()):
#     print(
#         "|"
#         + "  | \t   ".join(
#             [data["fname"][i],data["mname"][i],data["lname"][i],data["date"][i]]
#         )
#         + "|"
#     )
#     print("__________________________________________________________")
# fname = input("enter firt name ")
# mname = input("enter  middle name ")
# lname = input("enter last name ")
# date = time.asctime(time.localtime(time.time()))
# date = str(date)

# if data.get("fname"):
#     data["fname"].append(fname)
# else:
#     data["fname"] = [fname]
# if data.get("mname"):
#     data["mname"].append(mname)
# else:
#     data["mname"] = [mname]

# if data.get("lname"):
#     data["lname"].append(lname)
# else:
#     data["lname"] = [lname]

# if data.get("date"):
#     data["date"].append(date)
# else:
#     data["date"] = [date]
    
# name = input("Enter the name of the user whose data you want to update: ")
# fname = input("enter firt name ")
# mname = input("enter  middle name ")
# lname = input("enter last name ")
# date = time.asctime(time.localtime(time.time()))
# date = str(date)
# if name in data["fname"]:
#     index = data["fname"].index(name)
#     data["fname"][index] = fname
#     data["mname"][index] = mname
#     data["lname"][index] = lname
#     data["date"][index] = date
    
# else:
#     print(f"No user with name {name} found.")

# pdb.set_trace()
while True:
    name = input("Please give me the name of whose data update [q to quit]:")

    if name == 'q':
        break

    else:
       fname = input("enter the fname: ")
       mname = input("enter the middle name: ")
       lname= input("enter the last name: ")
       date= date = time.asctime(time.localtime(time.time()))
       date = str(date)
    # update data
       index = data["fname"].index(name)
       data["fname"][index]=fname
       data["mname"][index]=mname
       data["lname"][index]=lname
       data["date"][index]=date


json_data = json.dumps(data)
file = open("example.json", "w+")
file.write(json_data)




























