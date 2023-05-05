from akash.utils import load_data


data = load_data()


def list_records():
    print(
        "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Sno.",
            "fname",
            "mname",
            "lname",
            "date",
            "city",
        )
    )
    print(
        "________________________________________________________________________________________________"
    )

    for rec in data["records"]:
        record = data["records"][rec]
        print(
            "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                record["id"],
                record["first_name"],
                record["middle_name"],
                record["last_name"],
                record["date"],
                record["city"]
            )
        )
        print(
            "________________________________________________________________________________________________"
        )
    