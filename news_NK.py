#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from requests import post
from time import sleep


LOKI_URL = "https://api.droidtown.co/Loki/API/"
LOKI_CALL_URL = "https://api.droidtown.co/Loki/Call/"
USERNAME = "jennchang75@gmail.com"
LOKI_KEY = "SQG&lsQ+&@5lHy&21vB4N9JzeAZk2Fv"
POST_INTERVAL_SEC = 5

def getLokiTextSim(inputSTR, keywordLIST=[], featureLIST=[], count=1):
    payloadDICT = {
        "username": USERNAME,
        "loki_key": LOKI_KEY,
        "input_str": inputSTR,
        "keyword": keywordLIST,
        "feature": featureLIST,
        "count": count
    }

    while True:
        response = post(LOKI_URL, json=payloadDICT)
        if response.status_code == 200:
            try:
                resultDICT = response.json()
                if resultDICT["status"]:
                    if resultDICT["progress_status"] == "processing":
                        sleep(POST_INTERVAL_SEC)
                        continue
                return resultDICT
            except Exception as e:
                return {"status": False, "msg": str(e)}
        else:
            return {"status": False, "msg": "HTTP {}".format(response.status_code)}

def getInfo():
    payloadDICT = {
        "username": USERNAME,
        "loki_key": LOKI_KEY,
        "func": "get_info",
        "data": {}
    }

    response = post(LOKI_CALL_URL, json=payloadDICT)
    if response.status_code == 200:
        try:
            resultDICT = response.json()
            return resultDICT
        except Exception as e:
            return {"status": False, "msg": str(e)}
    else:
        return {"status": False, "msg": "HTTP {}".format(response.status_code)}

if __name__ == "__main__":
    from pprint import pprint

    inputSTR = 
    keywordLIST = []
    featureLIST = []
    countINT = 1

    resultDICT = getLokiTextSim(inputSTR, keywordLIST=keywordLIST, featureLIST=featureLIST, count=countINT)
    pprint(resultDICT)