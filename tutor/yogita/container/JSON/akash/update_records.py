from akash.utils import load_data, dump_data, input_records, Record
from akash.read_records import list_records


# from akash.create_record import create_records


def update_records():
    data = load_data()
    while True:
        name = input(
            "Please input `id` of the records you want to edit or [q to quit]:"
        )
        if name == "q":
            break
        else:
            fname, mname, lname ,city= input_records()
            rec = data["records"][name]
            fname = fname or rec["first_name"]
            mname = mname or rec["middle_name"]
            lname = lname or rec["last_name"]
            city = city or rec["city"]
            ch_rec = Record(fname, mname, lname,city, rec["id"], rec["date"])
            data["records"][name] = ch_rec.repr_str()
            dump_data(data)
