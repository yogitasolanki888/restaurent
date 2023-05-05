import smtplib
import requests
import datetime
import csv
from datetime import date


def get_messages():
    query_params = {
        "channel": "C03HGMADR3L",
        "oldest": 1681434024,
        "latest": 1681952424

    }
    headers = {
        "Authorization": "Bearer xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"
    }
    response = requests.get(
        "http://slack.com/api/conversations.history", headers=headers, params=query_params)

    return response.json().get("messages")


data = get_messages()
s_data = [{"user": x['user'], "text":x['text'],
           "ts":datetime.datetime.fromtimestamp(float(x['ts']))} for x in data]
data = s_data[::-1]
users_by_date = {}

for data_int in data:
    date = data_int["ts"].date()  # Extract the date from the timestamp

    if date not in users_by_date:
        users_by_date[date] = {}

    if data_int['user'] not in users_by_date[date]:
        if data_int["text"].lower() == "out":
            users_by_date[date][data_int['user']] = {
                "total_time": 0,
                "status": "out",
                "ts": data_int["ts"],
            }
        elif data_int["text"].lower() == "in":
            users_by_date[date][data_int['user']] = {
                "total_time": 30,
                "status": data_int["text"].lower(),
                "ts": 0,
            }
    else:
        if data_int["text"].lower() == "out" and users_by_date[date][data_int["user"]]["status"] == "out":
            users_by_date[date][data_int['user']]["total_time"] += 30
            users_by_date[date][data_int['user']]["ts"] = data_int["ts"]
            users_by_date[date][data_int['user']
                                ]["status"] = data_int["text"].lower()

        if data_int["text"].lower() == "out" and users_by_date[date][data_int['user']]["status"] == "in":
            users_by_date[date][data_int['user']
                                ]["status"] = data_int["text"].lower()
            users_by_date[date][data_int['user']]["ts"] = data_int["ts"]

        elif data_int["text"].lower() == "in" and users_by_date[date][data_int["user"]]["status"] == "in":
            users_by_date[date][data_int['user']]["total_time"] += 30
            users_by_date[date][data_int['user']]["ts"] = data_int["ts"]
            users_by_date[date][data_int['user']
                                ]["status"] = data_int["text"].lower()

        elif data_int["text"].lower() == "in" and users_by_date[date][data_int["user"]]["status"] == "out":
            in_time = data_int["ts"]
            out_time = users_by_date[date][data_int['user']]["ts"]
            total_break = (in_time - out_time).total_seconds() / 60
            users_by_date[date][data_int['user']]["total_time"] += total_break
            users_by_date[date][data_int['user']
                                ]["status"] = data_int["text"].lower()
            users_by_date[date][data_int['user']]["ts"] = data_int['ts']

for date, users in users_by_date.items():
    for user, user_data in users.items():
        if user_data['status'] == "out" and (datetime.datetime.now() - user_data['ts']).seconds > 1800:
            user_data["total_time"] += 30


def get_name(user_id):
    query_params = {

        "user": user_id
    }
    headers = {
        "Authorization": "Bearer xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"
    }

    response = requests.get(
        f"https://slack.com/api/users.profile.get", headers=headers, params=query_params)

    return response.json().get("profile")


result = {}
for date, ids in users_by_date.items():
    # print(date)
    for k, v in ids.items():
        # print(k,v)
        p = get_name(k)
        result[v['ts']] = {
            "name": p["real_name"],
            "email": p["email"],
            "total_break": v["total_time"]
        }
# print(result)


# Open a new CSV file in write mode
# with open('rty.csv', 'w') as csvfile:
#     # Create a writer object
#     writer = csv.writer(csvfile)
#     for dates,data in result.items():
#         for date in range(dates):
#     # Write the header row
#             writer.writerow(['Name', 'Email', date])
#             writer.writerow([data['name'], data['email'],data['total_time']] )

# with open('output_file.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for dates, data  in result.items():
#            row = ['name', 'email' , dates]
#            writer.writerow([data['name'],data["email"]])
# import csv

# # Read the input CSV file
# with open('input.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# Group the rows by name and date
# groups = {}
# for row in rows:
#     key = (row['Name'], row['Email'], row['Date'])
#     if key in groups:
#         groups[key] += int(row['Total time'])
#     else:
#         groups[key] = int(row['Total time'])

# # # Generate the output CSV file
# with open('output.csv', 'w', newline='') as f:
#     writer = csv.writer(f)

#     # Write the header row
#     writer.writerow(['Name', 'Email'] + sorted(set(row['Date'] for row in rows)))

#     # Write the data rows
    # for key, total_time in result.items():
    #     name, email, date = key
    #     row = [name, email]
    #     for d in sorted(set(row['Date'] for row in rows)):
    #         if d == date:
    #             row.append(total_time)
    #         else:
    #             row.append('')
    #     writer.writerow(row)

# import csv

# # sample data

# for dates ,data in result.items():
# # # prepare header row
#   header = ['name', 'email'] + list(dates[0][2].keys())

# write data to csv file
# with open('output.csv', mode='w') as files:
#     writer = csv.writer(files)
#     header=["name","email"]+[dates.strftime('%d/%m/%y') for dates, data in users_by_date.items()]
#     writer.writerow(header)
    # for k,v in result.items():
# #         writer.writerow([v['name'],v["email"],[data["total_break"] for dates, data in result.items()]])
#           row_data=[v['name'],v["email"] ]  + [data["total_break"] for dates, data in result.items()]
#           writer.writerow(row_data)

# -----------------------------------------------------------------------------------------------------------------
# read the CSV file and store the data in a dictionary
# data = {}
# for k , v in result.items():
#    if v["name"] not in data:
#        data[v["name"]]=v["email"]
    #    import pdb;pdb.set_trace()


# with open('output.csv', mode='w') as files:
#         writer = csv.writer(files)
#         header=["name","email"]+[dates.strftime('%d/%m/%y') for dates, data in users_by_date.items()]
#         writer.writerow(header)
#         for k,v in data.items():
#              writer.writerow([k,v])
# =====================================================================================================================

new_data = {}
for a, b in result.items():
    if b["name"] not in new_data:
        new_data[b["name"]] = b["email"]

l = []
for dates, data in users_by_date.items():
    l.append(dates.strftime('%d/%m/%y'))
with open('output.csv', mode='w') as files:
    writer = csv.writer(files)
    header = ["name", "email"] + \
        [dates.strftime('%d/%m/%y') for dates, data in users_by_date.items()]
    writer.writerow(header)
    # for key, value in result.items():
    #     for y in l:
    #         if y==(key.strftime("%d/%m/%y")):
    #             res=value["total_break"]

    for k, v in new_data.items():
        # row=[k,v] +[res]
        row = [k, v] + [value["total_break"] for key, value in result.items()
                        for y in l if y == key.strftime("%d/%m/%y") and k == value["name"]]
# ]
        # print(row)
        writer.writerow(row)
    #    writer.writerow([k,v] + [value["total_break"] for key,v alue in result.items() if y==key.strftime("%d%m%y") if y in result else None for y in l])


# for k,v in result.items():
#     print(v["total_break"])

def send_email():
    # Set up the email server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'yogitasolanki1200@gmail.com'
    smtp_password = 'gxmrjloymwyahzhs'
    smtp_sender = 'yogitasolanki1200@gmail.com'

# Loop through the result dictionary and send an email to each user
    for date, user_data in result.items():
        # Set up the email message
        recipient = user_data['email']
        subject = 'Your Break Report'
        body = f"Hi {user_data['name']},\n\nYour total break is of {date} {user_data['total_break']}."
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_sender, recipient, message)
        print(f"Email sent to {user_data['name']} ({user_data['email']})")
# send_email()
