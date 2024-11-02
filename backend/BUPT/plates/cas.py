from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

from ..constants import User_Agent, BUPT_CAS_LOGIN
from ..utlis.auto_retry import auto_retry_network_connections


class CAS:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._history = []
        self._login()

    def _get_session(self):
        session = requests.Session()
        session.headers["User-Agent"] = User_Agent
        return session

    @auto_retry_network_connections
    def _login(self):
        self.session = self._get_session()
        resp = self.session.get(url=BUPT_CAS_LOGIN)
        resp.raise_for_status()
        varid = BeautifulSoup(
            resp.text, "lxml"
        ).find(attrs={"name": "execution"})["value"]
        post_data = {
            "username": self.username,
            "password": self.password,
            "type": "username_password",
            "submit": "LOGIN",
            "_eventId": "submit",
            "execution": varid
        }
        resp = self.session.post(url=BUPT_CAS_LOGIN, data=post_data)
        resp.raise_for_status()

    @auto_retry_network_connections
    def get(self, *args, **kwargs):
        url = urlparse(kwargs.get("url", args[0])).netloc
        if url not in self._history:
            self._history.append(url)
            self.session.get(*args, **kwargs)
        return self.session.get(*args, **kwargs)

    @auto_retry_network_connections
    def post(self, *args, **kwargs):
        url = urlparse(kwargs.get("url", args[0])).netloc
        if url not in self._history:
            self._history.append(url)
            self.session.post(*args, **kwargs)
        return self.session.post(*args, **kwargs)
