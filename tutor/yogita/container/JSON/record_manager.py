from akash.read_records import list_records
from akash.create_record import create_records
from akash.update_records import update_records
from akash.delete_records import delete_records
from akash.add_new_record import add_new_record

# from akash.update_records import update_Record
import time


# print_file()
# create_records()
# update_records()
# delete_records()

# def operations():
#     while True:
#         print(
#             " press 1 for print_file \n press 2 for create_records \n press 3 for update_records \n press 4 for delete_records \n press 5 for add new key value \n press q for exit \n press 11 for updated_list"
#         )
#         press = input("press above key which you want to perform ")
       
#         if press == "1":
#             list_records()
#         elif press == "2":
#             create_records()
            
#         elif press == "3":
#             update_records()
            
#         elif press == "4":
#             delete_records()
           
#         elif press == "5":
#             add_new_record()

#         elif press == "q":
#             break
        

# operations()
def show():
    list_records()
    
def operations():
    while True:
        print(
            " press 1 for print_file \n press 2 for create_records \n press 3 for update_records \n press 4 for delete_records \n press 5 for add new key value \n press q for exit "
        )
        press = input("press above key which you want to perform ")
        if press == "1":
            show()
        elif press == "2":
            create_records()
            
        elif press == "3":
            update_records()
            
        elif press == "4":
            delete_records()
           
        elif press == "5":
            add_new_record()

        elif press == "q":
            break
operations()




