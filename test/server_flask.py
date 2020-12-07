import cv2
import numpy as np
import json
from flask import Flask, jsonify, request
from baseimg.img_b64 import image_to_base64

app1 = Flask(__name__)
@app1.route('/', methods=['POST'])
def create_task():
    print("Getting parameters.")
    json_data = request.get_json(force=True)

    img_json=json_data['base64']#传过来的json中的base64字段是我们需要的图像base64编码


    img_local = cv2.imread("qiaoba.jpg")
    img_local_j = image_to_base64(img_local)

    if img_json == img_local_j:
        feature_str = 'same base64 string, success.'
    else:
        feature_str = 'some error, fail.'

    out_json = {'code':'200','msg':'success!','feature':feature_str}#feature是你自己处理的结果
    return jsonify(out_json)

if __name__ == '__main__':
    app1.run(use_reloader=False, debug=True, host='127.0.0.1', port=5000, threaded=False)

