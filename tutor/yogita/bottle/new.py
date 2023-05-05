import json
import requests
from datetime import datetime
from datetime import *
from datetime import datetime, timedelta
import time


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
           "ts":datetime.fromtimestamp(float(x['ts']))} for x in data]
data = s_data[::-1]
# print(data)
import datetime

users = {}

import datetime

users = {}
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
            # user["total_time"] += (data_int["ts"] - user["ts"])
            users[data_int['user']]["status"] = data_int["text"].lower()
            users[data_int['user']]["ts"] = data_int['ts']
for x, y in users.items():
    if y['status'] == "out" and (datetime.datetime.now() - y['ts']).seconds > 1800:
        y["total_time"] += 30
# print(users)
def get_name(user_id):
    query_params = {
        # "channel": "C03HGMADR3L",
        # "oldest": 1681434000,
        "users": user_id
    }
    headers = {
        "Authorization": "Bearer xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"
    }

    response = requests.get(
        "https://slack.com/api/users.", headers=headers,params=query_params)
    # import pdb;pdb.set_trace()

    return response.json()

# for k, v in users.items():
#     p = get_name(k)
#     print(k, p["real_name"], p["email"],
#           "--------------------------------", v['total_time'],v['ts'])

# result={}
# for k, v in users.items():
#     p = get_name(k)
#     result[k] = {
#         "name": p["real_name"],
#         "email": p["email"],
#         "total_break": v["total_time"]
#     }

# print(result)




# # Get the messages from the Slack API
# def get_messages():
#     query_params = {
#         "channel": "C03HGMADR3L",
#         "oldest": 1681434042,
#         "latest": 1681952442

#     }
#     headers = {
#         "Authorization": "Bearer xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"
#     }
#     response = requests.get(
#         "http://slack.com/api/conversations.history", headers=headers, params=query_params)

#     return response.json().get("messages")

# data = get_messages()



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

print(users_by_date)
# print(users_by_date[datetime.date(2023, 4, 17)]['ABCD']['total_time'])

users = {}
for data_int in data:
    if data_int['user'] not in users:
        # import pdb; pdb.set_trace()
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

        # # # import pdb;pdb.set_trace()
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
            # user["total_time"] += (data_int["ts"] - user["ts"])
            users[data_int['user']]["status"] = data_int["text"].lower()
            users[data_int['user']]["ts"] = data_int['ts']
for x, y in users.items():
    if y['status'] == "out" and (datetime.now() - y['ts']).seconds > 1800:
        y["total_time"] += 30
