import os
from flask import Flask, request, Response


app = Flask(__name__)

SLACK_WEBHOOK_SECRET = "xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti"


# @app.route('/http://slack.com/api/conversations.history', methods=['GET'])
# def inbound():
#     if request.form.get('token') == SLACK_WEBHOOK_SECRET:
#         channel = request.form.get('status_update')
#         username = request.form.get('Anand_Kumar')
#         text = request.form.get('text')
#         inbound_message = username + " in " + channel + " says: " + text
#         print(inbound_message)
#     return Response(), 200


@app.route('http://slack.com/api/conversations.history', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)        