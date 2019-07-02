import base64
import http.client
from urllib import parse
from urllib import request
import cv2
import json
import numpy
import requests

def image_to_base64(image_np):

    image = cv2.imencode('.jpg',image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1]

    return image_code

img = cv2.imread("1.jpg")
data_bytes = image_to_base64(img)
data={"base64":data_bytes}
data = json.dumps(data)
logger.info(data)
url='http://127.0.0.1:5000/'
r = requests.post(url,data)
print(r.text)