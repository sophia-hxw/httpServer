#!/usr/bin/python3
#coding=utf-8
import json
import requests

import json
import requests

def send_request(data_b64):
    data={"base64":data_b64}
    data = json.dumps(data)
    
    url='http://127.0.0.1:5000/'
    r = requests.post(url,data)
    print(r.text)
    # print(r.json())
    


    