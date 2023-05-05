users={}
for data_int in data:
    if data_int['user'] not in users:
        if data_int["text"].lower() == "out":
            users[data_int['user']] = {
                "total_time": 0,
                "status": data_int["text"].lower(),
                "ts": data_int["ts"],
            }
        elif data_int["text"].lower() == "in":
            users[data_int['user']] = {
                "total_time": 1800,
                "status": data_int["text"].lower(),
                "ts": 0,
            }
    else:
        user = users[data_int['user']]
        if data_int["text"].lower() == "out" and user["status"] == "out":
            # User checked out twice in a row
            user["total_time"] += 1800  # Add 30 minutes to their total time
            user["ts"] = data_int["ts"]  # Update their timestamp
        elif data_int["text"].lower() == "out":
            if user["status"] == "in":
                # User checked out after checking in, subtract elapsed time
                user["total_time"] += (data_int["ts"] - user["ts"])
            user["status"] = data_int["text"].lower()
            user["ts"] = data_int["ts"]
        elif data_int["text"].lower() == "in" and user["status"] == "in":
            # User checked in twice in a row
            user["total_time"] += 1800  # Add 30 minutes to their total time
            user["ts"] = data_int["ts"]  # Update their timestamp
        elif data_int["text"].lower() == "in":
            if user["status"] == "out":
                # User checked in after checking out, add elapsed time
                user["total_time"] += (data_int["ts"] - user["ts"])
            user["status"] = data_int["text"].lower()
            user["ts"] = 0

# ---------------------------------------------------------------
 # else:
    #     # pass
    #     # import pdb;pdb.set_trace()
    #     if data_int["text"].lower() == "in" and users[data_int['user']]['status'].lower() == "out":
    #         # import pdb;pdb.set_trace()
    #         users[data_int['user']]['status'] = data_int["text"]
    #         in_time = data_int["ts"]
    #         out_time = users[data_int['user']]['ts']
    #         total_time = (in_time - out_time).total_seconds()/60
    #         users[data_int['user']]['total_time'] = total_time
#         elif data_int["text"].lower() == "out" and users[data_int['user']]['status'].lower() == "out":
#             pass
#         elif data_int["text"].lower() not in ["in", "out"]:
#             pass
        #         users[data_int['user']]['total_time']=1800

        # elif data_int["text"].lower() == "out" and users[data_int['user']['status']] == "in":
        #     out_time = data_int["ts"]
        #     in_time = users[data_int['user']]['ts']
        #     total_time= (in_time - out_time).total_seconds()/60
        #     users[data_int['user']]['total_time']= total_time
        # else:
        #     users[data_int['user']]['total_time']=1800

    # if data_int["text"].lower() == "out" and users[data_int['text']].lower() == "out":u
    #             users[data_int['status']]="out"
    #             users[data_int['ts']]= data_int['ts']
    #             out_time= data_int['ts']
    #             users[data_int['total_time']]=30
    # else:
    #     if data_int["text"].lower() == "out" and users[data_int['text']] == "in":
    #              out_time= users[data_int['ts']]
    #              in_time=user
    #              total_time= (in_time - out_time).total_seconds()/60
    #              users[data_int['total_time']]= total_time



    # for data_int in data:
    # if data_int['user'] not in users:
    #     if data_int["text"].lower() == "out":
    #         users[data_int['user']] = {
    #             "total_time": 0,
    #             "status": "out",
    #             "ts": data_int["ts"],
    #         }
    #     elif data_int["text"].lower() == "in":
    #         users[data_int['user']] = {
    #             "total_time": 30,
    #             "status": data_int["text"].lower(),
    #             "ts": 0,
    #         }
    # else:
    #     user_data = users[data_int['user']]
    #     if data_int["text"].lower() == "out" and user_data["status"] == "in":
    #         # User forgot to text "in", add 30 minutes to total time
    #         user_data["total_time"] += 30
    #         user_data["status"] = "out"
    #         user_data["ts"] = data_int["ts"]
    #     elif data_int["text"].lower() == "in":
    #         user_data["status"] = "in"
    #         user_data["ts"] = 0
