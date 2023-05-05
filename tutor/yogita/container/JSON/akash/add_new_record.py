from akash.utils import load_data, dump_data, input_records, Record

# from akash.create_record import create_records


# def add_new_record():
#     data = load_data()
#     while True:
#         name = input(
#             "Please input `id` of the records you want to add new field or [q to quit]:"
#         )
#         if name == "q":
#             break
#         else:
#             # fname, mname, lname = input_records()
#             add_key = input("Enter  new key name: ")
#             add_value = input("Enter new value name : ")
#             rec = data["records"][name]
#             rec[add_key.title()] = add_value

#             dump_data(data)

def add_new_record():
    data = load_data()
    add_key= input("enter key")
    add_val=input("enter value")
    for key in data["records"].keys():
       data["records"][key][add_key]=add_val

    dump_data(data)

