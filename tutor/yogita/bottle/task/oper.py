# client: 1) insert
#         2) update
#         3) search
#         4) Delete
#         5) Get

# lis = [] arry
# set =set{}
# tup = ()
# dict = {}
def input_data():
    print("\n\n Enter details\n\n")
    fname = input("enter first name")
    mname = input("enter middle  name")
    lname = input("enter last name")
    return fname, mname, lname


class Operations:
    def __init__(self, fname, mname, lname, id=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.id = id

    def __str__(self):
        return f" {self.fname} {self.mname} {self.lname}"

    def repr_str(self):
        return {
            "id": self.id if self.id else None,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
        }

    def create():
        fname, mname, lname = input_data()
        rec = Operations(fname, mname, lname,)
        rec.id = int() + 1
        ["records"][str(rec.id)] = rec.repr_str()

    def update():
        while True:
            name = input(
                "Please input `id` of the records you want to edit or [q to quit]:"
                )
            if name == "q":
                break
            else:
                fname, mname, lname, city = input_data()
                rec = ["records"][name]
                fname = fname or rec["first_name"]
                mname = mname or rec["middle_name"]
                lname = lname or rec["last_name"]
                city = city or rec["city"]
                ch_rec = Operations(fname, mname, lname, rec["id"],)
                ["records"][name] = ch_rec.repr_str()

    def delete():
        while True:
            name = input(
                "Please input `id` of the records you want to delete [q to quit]:")
            if name == "q":
                break
            else:
             # fname, mname, lname = input_records()
                del ["records"][name]
# def search():
#     pass

# def get():
#     pass
obj=Operations("yogita","abc","solanki")
obj.create()
obj.update()
obj.delete()






# def perform():
#     while True:
#         print(
#              " press 1 for print_file \n press 2 for create_records \n press 3 for update_records \n press 4 for delete_records " )
#         press = input("press above key which you want to perform ")

#         if press == "1":
#             # list_records()
#              pass
#         elif press == "2":
#             create()

#         elif press == "3":
#             update()

#         elif press == "4":
#             delete()

#         elif press == "q":
#              break
# perform()


# obj =  Operations()
