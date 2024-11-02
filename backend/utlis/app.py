from flask import Flask
from flask_cors import CORS
import requests
import json


app = Flask("Dormitory_Helper")
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://BUPT:mysql-bupt-pswd@localhost/BUPT_Helper'
from .db import User


@app.route('/login')
def login():
    stmt = User

def get_info(session: requests.Session, data):
    url = get_url_list()
    session.get(url["bupt"]["wxapp"]["elec"]["chong"])
    resp = session.post(url["bupt"]["wxapp"]["elec"]["search"], data=data)
    try:
        data = json.loads(resp.text)["d"]["data"]
        surplus = data["surplus"]
        updateTime = data["time"]
    except json.JSONDecodeError:
        print("JSONDecodeError")
    else:
        print(f"更新时间:{updateTime}，剩余电量：{surplus}")
        return [updateTime, surplus]
