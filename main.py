## 测试http的客户端和flask及uwsgi的服务端，传送的数据是图片的base64编码
def test_flask_cs():
    import cv2
    from test.http_client import send_request
    from baseimg.img_b64 import image_to_base64

    img_pth = "data/img/boniu.jpg"
    img = cv2.imread(img_pth)
    data_bytes = image_to_base64(img)
    
    send_request(data_bytes)

# 测试四种不同形式的python配置文件
def test_params_file():
    from test.params_file import config_ini,config_json,config_toml,config_yaml

    ifile_pth = "./data/params_file/sample.ini"
    jfile_pth = "./data/params_file/sample.json"
    tfile_pth = "./data/params_file/sample.toml"
    yfile_pth = "./data/params_file/sample.yaml"
    config_block = "sample1"

    ini_res = config_ini(ifile_pth, config_block)
    print("ini params: ", ini_res)

    json_res = config_json(jfile_pth, config_block)
    print("json params: ", json_res)

    toml_res = config_toml(tfile_pth, config_block)
    print("toml params: ", toml_res)

    yaml_res = config_yaml(yfile_pth, config_block)
    print("yaml params: ", yaml_res)


if __name__ == "__main__":
    # test_flask_cs()
    test_params_file()