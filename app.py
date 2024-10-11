from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import threading
import requests
import time
import json
import os

from utlis.bupt_auth import BUPT_CAS
from utlis.url import get_url_list


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    remaining = db.Column(db.Float)


@app.route('/data')
def get_data():
    data = DataPoint.query.order_by(DataPoint.timestamp.desc()).all()
    return jsonify([
        {
            'timestamp': dp.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'remaining': dp.remaining
        } for dp in data
    ])


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


def update_data():
    config_file = os.path.join(os.path.dirname(__file__), "config/bupt.json")
    with open(config_file, "r") as f:
        config = json.load(f)
    cas = BUPT_CAS(config["cas"]["username"], config["cas"]["password"], CAS=True)
    sleeptime = 600
    while True:
        timestamp, remaining = get_info(cas.session, config["info"])
        if remaining < 10 and sleeptime == 600:
            sleeptime = 60
        else:
            sleeptime = 600
        timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        new_data = DataPoint(timestamp=timestamp, remaining=remaining)
        with app.app_context():
            db.session.add(new_data)
            db.session.commit()
        time.sleep(sleeptime)


def monitor():
    thread = threading.Thread(name="update_data", target=update_data)
    thread.start()
    restart_attempts = 0
    max_restart_attempts = 5

    while True:
        thread.join()
        restart_attempts += 1
        print(f"Thread {thread.name} restarted {max_restart_attempts} times.")

        if restart_attempts >= max_restart_attempts:
            print(f"Thread {thread.name} restarted {max_restart_attempts} times. Pausing for 5 minutes.")
            time.sleep(300)
            restart_attempts = 0

        thread = threading.Thread(name="update_data", target=update_data)
        thread.start()


def main():
    with app.app_context():
        db.create_all()
    monitor_thread = threading.Thread(name="monitor", target=monitor, daemon=True)
    monitor_thread.start()
    app.run(host="0.0.0.0")


main()
