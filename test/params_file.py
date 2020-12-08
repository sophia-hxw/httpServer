# TODO: 将配置文件写成python的一个类
def config_ini(file_pth, config_block):
    import os
    from configparser import ConfigParser

    dict_params = {}
    if os.path.exists(file_pth):
        cfg = ConfigParser() 
        cfg.read(file_pth)
        params = cfg.items(config_block)
        # print(type(params)) #class 'list'
        dict_params = dict(params)
        # print(dict_params)

    return dict_params

def config_json(file_pth, config_block):
    import os
    import json

    res_params = {}
    if os.path.exists(file_pth):
        with open(file_pth) as j:
            params = json.load(j)
            res_params = params[config_block]

    return res_params

def config_yaml(file_pth, config_block):
    import os
    import yaml

    res_params = {}
    if os.path.exists(file_pth):
        with open(os.path.expanduser(file_pth), "r") as config: 
            params = yaml.safe_load(config)
            res_params = params[config_block]
    
    return res_params

def config_toml(file_pth, config_block):
    import toml 
    import os

    res_params = {}
    if os.path.exists(file_pth):
        params = toml.load(os.path.expanduser(file_pth))
        res_params = params[config_block]

    return res_params

if __name__== "__main__":
    pass
