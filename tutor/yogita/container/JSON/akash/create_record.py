from akash.utils import load_data, dump_data, input_records, Record


def create_records():
    data = load_data()
    fname, mname, lname ,city = input_records()
    rec = Record(fname, mname, lname,city)
    pk = data["meta"]["last_id"]

    rec.id = int(pk) + 1
    data["records"][str(rec.id)] = rec.repr_str()
    data["meta"]["last_id"] = str(rec.id)

    # data["data"].append(rec.repr_str())
    # data["data"] = rec.repr_str()
    dump_data(data)
    