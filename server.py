import json
from flask import Flask, jsonify, request

app1 = Flask(__name__)
@app1.route('/', methods=['POST'])
def create_task():
    print("Getting json")
    json_data = request.get_json(force=True)

    img_json=json_data['base64']    #传过来的json中的base64字段是我们需要的图像base64编码

    img_regis = base64_to_image(img_json)
    img = img_regis[:,:,0:3]
    if img is None:
        print("Not a real image.")

'''
your program
'''

    feature_str =''
    for i in feature:
        if not feature_str == '':
            feature_str = feature_str+','+str(i)
        else: 
            feature_str = str(i)

    out_json = {'code':'200','msg':'success!','feature':feature_str}#feature是你自己处理的结果
    return jsonify(out_json)


if __name__ == '__main__':
    app1.run(use_reloader=False, debug=True, host='127.0.0.1', port=5000, threaded=False)

