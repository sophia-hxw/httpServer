from flask import Flask, jsonify, request
from baseimg.img_b64 import base64_to_image

app1 = Flask(__name__)
@app1.route('/', methods=['POST'])
def create_task():
    print("Getting parameters.")
    json_data = request.get_json(force=True)

    img_b64=json_data['base64']
    out_json = {'code':'200','msg':'success!','result':""}#feature是你自己处理的结果

    ##### 自己的服务端处理代码
    img = base64_to_image(img_b64)

    if not img is None:
        res_status = 'b64->img, success.'
    else:
        res_status = 'b64->img, fail.'
    ##### 自己的服务端处理代码

    out_json["result"] = res_status
    return jsonify(out_json)

if __name__ == '__main__':
    app1.run(use_reloader=False, debug=True, host='127.0.0.1', port=5000, threaded=False)

