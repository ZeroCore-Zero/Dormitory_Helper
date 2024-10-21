from bs4 import BeautifulSoup
import requests
import time

from .logger import MyLogger
from .url import get_url_list


class BUPT_CAS:
    MAX_RETRY = 5
    NAME = "BUPT_CAS"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

    def __init__(self, username, password, CAS=False):
        self.username = username
        self.password = password
        self._url = get_url_list()
        self._log = MyLogger(BUPT_CAS.NAME)
        self.session = self._session_init(CAS=CAS)

    def _session_init(self, *, CAS=False) -> requests.Session:
        """
            初始化一个requests.Session对象，清除初始header并设置UA

            返回值：
            session：   requests.Session对象
        """
        session = requests.Session()
        session.headers.clear()
        session.headers['User-Agent'] = BUPT_CAS.USER_AGENT
        if not CAS:
            self._log.debug("不登入CAS")
            return session

        self._log.debug("请求登入CAS")
        is_success = False
        for i in range(1, BUPT_CAS.MAX_RETRY + 1):
            try:
                resp = session.get(url=self._url["bupt"]["cas"])
                resp.raise_for_status()
                varid = BeautifulSoup(
                    resp.text, "html.parser"
                ).find(attrs={"name": "execution"})["value"]
                post_data = {
                    "username": self.username,
                    "password": self.password,
                    "type": "username_password",
                    "submit": "LOGIN",
                    "_eventId": "submit",
                    "execution": varid
                }
                resp = session.post(url=self._url["bupt"]["cas"], data=post_data)
                resp.raise_for_status()
            except requests.exceptions.ConnectionError as e:
                self._log.error(e)
                self._log.error(f"网络连接错误，第{i}次")
            except requests.exceptions.HTTPError as e:
                self._log.error(e)
                self._log.error(f"HTTP错误，第{i}次")
            else:
                self._log.debug("成功登入CAS")
                is_success = True
            finally:
                if is_success:
                    return session
                if i < BUPT_CAS.MAX_RETRY:
                    self._log.error(f"等待重试第{i + 1}次")
                    time.sleep(3)
                else:
                    self._log.error("达到最大重试次数，登录失败")
        return None
