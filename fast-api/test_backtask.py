# -*- encoding: utf-8 -*-
# Author: li_colin
import requests

ret = requests.post("http://127.0.0.1:8000/send-notification/foo@example.com")

print(ret.json())
print(ret.status_code)
