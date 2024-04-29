#! /usr/bin/env python3

import requests
import sys

def load_token(token_path:str='')-> str:
    """
    Open token path for reading and return token.

    @param token_path: a valid path to the file
    @return token: the contents of the file
    """
    with open(token_path,'r') as tfile:
        return tfile.read().strip()

def pomo_announce(token:str='', server:str='', topic:str='', reps:int=0) -> dict:
    """
    Use the notify API to announce that the pomo is done.

    @param token: a valid token
    @param server: a notify server
    @param topic: the topic to publish to
    @param reps: how many reps of the pomodoro have been done
    @return result: what request said we got
    """
    result = requests.post(f"{server}{topic}", \
        data = sys.argv[1].encode(encoding="utf-8"), \
        headers = {
            "Title": "POMO DONE",
            "Priority": "urgent",
            "Authorization": f"Bearer {token}"
    })
    return result

def main():
    BASE_URL = str()
    TOPIC = str()
    TOKEN_PATH = str()
    TOKEN = load_token(TOKEN_PATH)
    REPS = 100

    r = pomo_announce(token=TOKEN, server=BASE_URL, topic=TOPIC, reps=REPS)

if __name__ == "__main__":
    main()
