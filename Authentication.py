import requests
from requests.auth import AuthBase
from urllib.parse import urlparse
from base64 import b64encode
import hmac
import hashlib
import time


class HS256(AuthBase):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        url = urlparse(r.url)
        timestamp = str(int(time.time()))
        msg = r.method + timestamp + url.path
        if url.query != "":
            msg += "?" + url.query
        if r.body:
            msg += r.body

        signature = hmac.new(self.password.encode(), msg.encode(), hashlib.sha256).hexdigest()
        auth_str = "HS256 " + b64encode(
                    b':'.join((self.username.encode(), timestamp.encode(), signature.encode()))).decode().strip()

        r.headers['Authorization'] = auth_str
        return r

