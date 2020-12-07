#!/usr/bin/python3
#coding=utf-8
import json
from flask import Flask, jsonify, request
from baseimg.img_b64 import base64_to_image
from gevent import pywsgi

app1 = Flask(__name__)
@app1.route('/', methods=['POST'])
def create_task():
    print("Getting json")
    json_data = request.get_json(force=True)

    img_json=json_data['base64']    #传过来的json中的base64字段是我们需要的图像base64编码

    img_regis = base64_to_image(img_json)
    img = img_regis[:,:,0:3]
    out_json = {'code':'200','error_msg':''}
    if img is None:
        print("Not a real image.")
        out_json['isimg']=False
    else:
        out_json['isimg']=True

    '''
    your program
    '''
    return jsonify(out_json)


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 12151), app1)
    server.serve_forever()
    #app1.run(use_reloader=False, debug=True, host='127.0.0.1', port=5000, threaded=False)

