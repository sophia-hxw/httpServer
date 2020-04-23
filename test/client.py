#!/usr/bin/python3
#coding=utf-8
import cv2
import json
import requests
import sys
sys.path.append("..")
from baseimg.img_b64 import image_to_base64
from config.logs import Log


if __name__ == "__main__":
    logger = Log(logfilename='clients.log')

    img = cv2.imread("qiaoba.jpg")
    data_bytes = image_to_base64(img)
    data={"base64":data_bytes}
    data = json.dumps(data)
    logger.info(data)
    url='http://127.0.0.1:5000/'
    r = requests.post(url,data)
    print(r.text)
    # print(r.json())