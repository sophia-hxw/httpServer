import cv2
import json
import requests

img = cv2.imread("1.jpg")
data_bytes = image_to_base64(img)
data={"base64":data_bytes}
data = json.dumps(data)
logger.info(data)
url='http://127.0.0.1:5000/'
r = requests.post(url,data)
print(r.text)
# print(r.json())