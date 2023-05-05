
# import datetime

# users = {}
# for item in data:
#     user = item['user']
#     if user not in users:
#         users[user] = {'out_count': 0, 'in_count': 0, 'total_break_time': datetime.timedelta()}
#     if item['text'].lower() == 'out':
#         users[user]['out_count'] += 1
#         out_ts = item['ts']
#     elif item['text'].lower() == 'in':
#         users[user]['in_count'] += 1
#         in_ts = item['ts']
#         break_time = in_ts - out_ts
#         users[user]['total_break_time'] += break_time

# # print results
# for user, data in users.items():
#     print(f"User {user} went out {data['out_count']} times and came in {data['in_count']} times.")
#     print(f"Total break time for {user}: {data['total_break_time']}")


# 2)
# break_time = {}

# # sort the data by timestamp
# data_sorted = sorted(data, key=lambda x: x['ts'])

# # initialize the last status and timestamp for the first user
# last_status = data_sorted[0]['text']
# last_ts = data_sorted[0]['ts']

# # iterate over the sorted data
# for d in data_sorted:
#     user = d['user']
#     status = d['text']
#     ts = d['ts']
    
#     # calculate the time difference between the current and last timestamps
#     time_diff = ts - last_ts
    
#     # update the break time for the current user if necessary
#     if status == 'in' and last_status == 'out':
#         if user in break_time:
#             break_time[user] += time_diff
#         else:
#             break_time[user] = time_diff
    
#     # update the last status and timestamp for the current user
#     last_status = status
#     last_ts = ts
    
# # print out the total break time for each user
# for user, time in break_time.items():
#     print(f'{user}: {time}')


# 3

from datetime import datetime


# status = {}
# break_time = {}

# for item in data:
#     user = item['user']
#     text = item['text']
#     ts = item['ts']
    
#     if user not in status:
#         status[user] = 'out'
#         break_time[user] = 0
    
#     if text.lower() == 'in' and status[user] == 'out':
#         diff = ts - status_ts
#         break_time[user] += diff.seconds // 60
#     elif text.lower() == 'out':
#         status[user] = 'out'
#         status_ts = ts
#     elif text.lower() == 'in':
#         status[user] = 'in'

# # print break time for each user
# for user, time in break_time.items():
#     print(f"User {user} took a break for {time} minutes.")

# 4

# from datetime import datetime

# # Initialize dictionaries to store the in and out times and the total time for each user
# in_times = {}
# out_times = {}
# total_times = {}

# # Iterate through the data list
# for event in data:
#     # Get the user, status, and time from the current event
#     user = event['user']
#     status = event['text']
#     ts= event['ts']
    
#     # Update the in_times dictionary if the user checks in
#     if status == 'in':
#         in_times[user] = ts
#     # Update the out_times and total_times dictionaries if the user checks out
#     elif status == 'out':
#         # Calculate the time difference between the check-in and check-out times
#         time_diff = ts - in_times[user]
#         # Add the time difference to the total time for the user
#         total_times[user] = total_times.get(user, datetime.min) + time_diff
#         # Add the current check-out time to the out_times dictionary
#         out_times[user] = ts

# # Print the in and out times and total time for each user
# for user in in_times:
#     print(f"{user}:")
#     print(f"  In time: {in_times[user].strftime('%H:%M')}")
#     print(f"  Out time: {out_times[user].strftime('%H:%M')}")
#     print(f"  Total time: {total_times[user].strftime('%H:%M')}")

# 5

# for x in data:
# data = [
#     {'user': 'John', 'status': 'in', 'time': '9:00'},
#     {'user': 'Sara', 'status': 'in', 'time': '9:05'},
#     {'user': 'John', 'status': 'out', 'time': '9:30'},
#     {'user': 'Sara', 'status': 'out', 'time': '9:35'},
#     {'user': 'John', 'status': 'in', 'time': '10:00'},
#     {'user': 'Sara', 'status': 'in', 'time': '10:05'},
#     {'user': 'John', 'status': 'out', 'time': '10:30'},
#     {'user': 'Sara', 'status': 'out', 'time': '10:35'}
# ]

# out_count = {}
# break_count = 0

# for row in data:
#     user = row['user']
#     status = row['text']
    
#     if status == 'out':
#         if user not in out_count:
#             out_count[user] = 1
#         else:
#             out_count[user] += 1
            
#     elif status == 'in':
#         if user in out_count:
#             out_count[user] -= 1
            
#     if len(out_count) > 0:
#         break_count += 1
        
# print("Number of times each user went out:")
# for user, count in out_count.items():
#     print(f"{user}: {count}")
    # print(f"Total number of breaks: {break_count}")




