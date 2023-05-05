from akash.utils import load_data, dump_data, input_records, Record


def delete_records():
    data = load_data()
    while True:
        name = input("Please input `id` of the records you want to delete [q to quit]:")
        if name == "q":
            break
        else:
            # fname, mname, lname = input_records()
            del  data["records"][name]
            dump_data(data)
