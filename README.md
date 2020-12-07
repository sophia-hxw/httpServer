# 代码说明

# 功能说明
## 简单的http服务和客户端框架
两种服务端，都在test文件夹内，其中，server_flask是用经典的flask起的服务，而server_uwsgi则用wsgi包装了一层，具体有啥区别呢？起过flask服务的小伙伴应该见过这个警告：
```
 WARNING: This is a development server. Do not use it in a production deployment.
```
而用uwsgi则木有这个警告哦，具体的细节，可以去查看二者的源码。

使用方法：
- 启动第一个终端cd repo/test
- 运行服务端代码python3 server_flask.py 或者是python3 server_uwsgi.py
- 启动第二个终端cd repo/
- 运行客户端代码python3 main.py

注意：实际客户端处理细节在test/http_client.py
 

## 日志模块
- [ ] log模块  

## python中的几种参数配置文件
- [ ] ini
- [ ] json
- [ ] toml
- [ ] yaml