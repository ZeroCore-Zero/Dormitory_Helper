from utlis.bupt_auth import BUPT_CAS
import json
import os


def get_info(session, data):
    url = "https://app.bupt.edu.cn/buptdf/wap/default/search"
    cookies = {
        "eai-sess": "k55vl4gsvks1m58khbbflk5be5",
        "UUkey": "0b2cae3f3c0dcbd75ee298334ead819a"
    }
    resp = session.post(url, data=data, cookies=cookies)
    try:
        data = json.loads(resp.text)["d"]["data"]
        surplus = data["surplus"]
        updateTime = data["time"]
    except json.JSONDecodeError:
        print("JSONDecodeError")
    else:
        print(f"更新时间:{updateTime}，剩余电量：{surplus}")
        return [updateTime, surplus]


def main():
    config_file = os.path.join(os.path.dirname(__file__), "config/bupt.json")
    with open(config_file, "r") as f:
        config = json.load(f)
    cas = BUPT_CAS(config["cas"]["username"], config["cas"]["password"], CAS=True)
    get_info(cas.session, config["info"])


if __name__ == '__main__':
    main()
