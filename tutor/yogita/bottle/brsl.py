import pdb
from email.message import EmailMessage
import ssl
import smtplib
import time
import json
import requests
import datetime
# from datetime import *
# from datetime import datetime


def get_messages():
    query_params = {
        "channel": "C03HGMADR3L",
        "oldest": 681434024,
        "latest": 1681952424

    }
    headers = {
        "Authorization": "Bearer xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"
    }
    response = requests.get(
        "http://slack.com/api/conversations.history", headers=headers, params=query_params)

    return response.json().get("messages")


data = get_messages()
# print(data)
s_data = [{"user": x['user'], "text":x['text'],
           "ts":datetime.datetime.fromtimestamp(float(x['ts']))} for x in data]
data = s_data[::-1]
print(data)
users = {}
# Loop through the data and update the dictionary
for data_int in data:
    if data_int['user'] not in users:
        if data_int["text"].lower() == "out":
            users[data_int['user']] = {
                "total_time": 0,
                "status": "out",
                "ts": data_int["ts"],
            }
        elif data_int["text"].lower() == "in":
            users[data_int['user']] = {
                "total_time": 30,
                "status": data_int["text"].lower(),
                "ts": 0,
            }
    else:
        if data_int["text"].lower() == "out" and users[data_int["user"]]["status"] == "out":
            users[data_int['user']]["total_time"] += 30
            users[data_int['user']]["ts"] = data_int["ts"]
            users[data_int['user']]["status"] = data_int["text"].lower()

        if data_int["text"].lower() == "out" and users[data_int['user']]["status"] == "in":
            users[data_int['user']]["status"] = data_int["text"].lower()
            users[data_int['user']]["ts"] = data_int["ts"]

        elif data_int["text"].lower() == "in" and users[data_int["user"]]["status"] == "in":
            users[data_int['user']]["total_time"] += 30
            users[data_int['user']]["ts"] = data_int["ts"]
            users[data_int['user']]["status"] = data_int["text"].lower()

        elif data_int["text"].lower() == "in" and users[data_int["user"]]["status"] == "out":
            in_time = data_int["ts"]
            out_time = users[data_int['user']]["ts"]
            total_break = (in_time-out_time).total_seconds()/60
            users[data_int['user']]["total_time"] += total_break
            users[data_int['user']]["status"] = data_int["text"].lower()
            users[data_int['user']]["ts"] = data_int['ts']

# Update total_time for users who are still "out" after 30 minutes
for x, y in users.items():
    if y['status'] == "out" and (datetime.datetime.now() - y['ts']).seconds > 1800:
        y["total_time"] += 30

# Create a new dictionary to store the data in date-wise key-value pairs
users_by_date = {}

# Loop through the users dictionary and update the users_by_date dictionary
for x, y in users.items():
    date = y["ts"].date()
    if date not in users_by_date:
        users_by_date[date] = {x: y}
    else:
        users_by_date[date][x] = y

# Print the users_by_date dictionary
print(users_by_date)





















# for message in data:
#     if message['user'] not in users:
#         users[message['user']] = {}
#     if message['text'].lower() == "out":
#         users[message['ts']] = message['ts']
#         if users[message['user']].get('status') == 'in':
#             users[message['user']]['status'] = 'out'
#         elif users[message['user']].get('status') == 'out':
#             users[message['user']]['status'] = 'out'
#         else:
#             users[message['user']]['status'] = 'out'

#     elif message['text'].lower() == "in":
#         users[message['ts']] = message['ts']
#         if users[message['user']].get('status') == 'in':
#             users[message['user']]['status'] = 'in'
#         elif users[message['user']].get('status') == 'out':
#             users[message['user']]['status'] = 'in'
#         else:
#             users[message['user']]['status'] = 'in'
#     else:
#         ...

# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)
# for data_int in data:
#     if data_int['user'] not in users:
#         # import pdb; pdb.set_trace()
#         if data_int["text"].lower() == "out":
#             users[data_int['user']] = {
#                 "total_time": 0,
#                 "status": "out",
#                 "ts": data_int["ts"],
#             }
#         elif data_int["text"].lower() == "in":
#             users[data_int['user']] = {
#                 "total_time": 30,
#                 "status": data_int["text"].lower(),
#                 "ts": 0,
#             }
#     else:

#         # # # import pdb;pdb.set_trace()
#         if data_int["text"].lower() == "out" and users[data_int["user"]]["status"] == "out":
#             users[data_int['user']]["total_time"] += 30
#             users[data_int['user']]["ts"] = data_int["ts"]
#             users[data_int['user']]["status"] = data_int["text"].lower()

#         if data_int["text"].lower() == "out" and users[data_int['user']]["status"] == "in":
#             users[data_int['user']]["status"] = data_int["text"].lower()
#             users[data_int['user']]["ts"] = data_int["ts"]

#         elif data_int["text"].lower() == "in" and users[data_int["user"]]["status"] == "in":
#             users[data_int['user']]["total_time"] += 30
#             users[data_int['user']]["ts"] = data_int["ts"]
#             users[data_int['user']]["status"] = data_int["text"].lower()

#         elif data_int["text"].lower() == "in" and users[data_int["user"]]["status"] == "out":
#             in_time = data_int["ts"]
#             out_time = users[data_int['user']]["ts"]
#             total_break = (in_time-out_time).total_seconds()/60
#             users[data_int['user']]["total_time"] += total_break
#             # user["total_time"] += (data_int["ts"] - user["ts"])
#             users[data_int['user']]["status"] = data_int["text"].lower()
#             users[data_int['user']]["ts"] = data_int['ts']

        # elif data_int["text"].lower() != "in" and users[data_int["user"]]["status"] == "out":
        #     current_time = datetime.now()
        #     total_break = (
        #         current_time - users[data_int['user']]["ts"]).total_seconds()/60
        #     users[data_int['user']]["total_time"] += total_break

# print(users)

# for x, y in users.items():
#     if y['status'] == "out" and (datetime.now() - y['ts']).seconds > 1800:
#         y["total_time"] += 30


# def get_name(k):
#     query_params = {
#         # "channel": "C03HGMADR3L",
#         # "oldest": 1681434000,
#         # "users": user
#     }
#     headers = {
#         "Authorization": "Bearer xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"
#     }

#     response = requests.get(
#         f"https://slack.com/api/user.profile/{k}", headers=headers)
#     # import pdb;pdb.set_trace()

#     return response.json()


# username = get_name()
# # print(username)

# # with open('user.json', 'w') as f:
# #   json.dump( username, f )
# # print(username)

# for name in username["members"]:
#    for k,v in users.items():
#     # import pdb
#     get_name(k)
#     pdb.set_trace()
#     if name["id"] == user:
#         print(user, name["real_name"],
#                   "--------------------------------", break_time['total_time'])
# pdb.set_trace()

# for user, break_time in users.items():
#     print(get_name(user), "-----------", break_time['total_time'])


# for x in username["members"]:
#     for user in users:
#         if x["id"] == user:
#             print(user,x["name"]+"@gmail.com")
# ----------------------------------------------------------------------------------------------------------------------------------
# send email

# # Define email sender and receiver
# email_sender = 'yogitasolanki1200@gmail.com'
# email_password = input(" Enter your email password ")
# email_receiver = 'by242862@gmail.com'

# # Set the subject and body of the email
# subject = 'Remainder Forgot to return in'
# body = """
# forgot to return in after going out."
# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# # Add SSL (layer of security)
# context = ssl.create_default_context()

# # Log in and send the email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())


# xl = {'U02P77MML3T': {'total_time': 60, 'status': 'out',
#                       'ts': datetime.datetime(2023, 4, 14, 17, 52, 37, 123449)}}
