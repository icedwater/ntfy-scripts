#! /usr/bin/env python3

"""
From the pomofocus webhook, send an alert when a round ends.
"""

from flask import Flask, request
import requests
from pomoself import load_token, pomo_announce as announce
from pomoself import BASE_URL, TOPIC, TOKEN_PATH
TOKEN = load_token(TOKEN_PATH)

app = Flask(__name__)

# @app.route("/bloop", methods=["POST"])
# def pingme():
#     result = announce(title="Test", text=request.json, token=TOKEN, server=BASE_URL, topic="alarms")
#     return str(result)

@app.route('/tomato', methods=["POST"])
def result():

    """
    {
        'round': 'pomodoro' | 'short_break' | 'long_break',
        'type': 'pause' | 'start' | 'finish',
        'project': None | 'name',
        'task': 'task_name',
        'session_start': None | unix_timestamp_int,
        'session_end': None | unix_timestamp_int,
        'seconds': session_end - session_start
    }
    """

    round_type = ["pomodoro", "short_break", "long_break"]
    msg = str()

    data = request.json
    project = data["project"]
    task = data["task"]
    current_task = f"({project}) {task}"
    result = ''

    if data["type"] == "finish":
        if data["round"] == round_type[0]:
            msg = f"Congratulations on another step."
        elif data["round"] == round_type[1]:
            msg = f"Well, back to work..."
        elif data["round"] == round_type[2]:
            msg = f"Good stretch?"

        result = announce(title=current_task, text=msg, token=TOKEN, server=BASE_URL, topic=TOPIC)
    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=45092)
