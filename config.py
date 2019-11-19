from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://ygh:yGh@=513!@192.168.182.131:3306/myweb"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://YgH1:YgH1@513!@192.168.182.129:3306/myflask"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
# db = SQLAlchemy(app)