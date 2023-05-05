from akash.records_schema import FIELDS
from datetime import datetime
import json


class Record:
    def __init__(self, first_name, middle_name, last_name, city, id=None, ts=None) -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.ts = datetime.now()
        self.id = id
        self.city = city

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name} {self.ts} {self.city}"

    def repr_str(self):
        return {
            "id": self.id if self.id else None,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "date": self.ts.__str__(),
            "city":self.city,
        }


def load_data(file="records.json"):
    with open(file, "r") as myfile:
        data = myfile.read()
    return json.loads(data)


def dump_data(data, file="records.json"):
    json_data = json.dumps(data)
    file = open(file, "w+")
    file.write(json_data)


def input_records():
    print("\n\n Enter details\n\n")
    fname = input("enter firt name ")
    mname = input("enter  middle name ")
    lname = input("enter last name ")
    city= input("enter city ")
    return fname, mname, lname ,city
