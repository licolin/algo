# -*- encoding: utf-8 -*-
# Author: li_colin

class HTTPHandler:
    def handle(self, request):
        methname = request.method
        print(getattr(self, methname))
        getattr(self, methname)()

    def GET(self):
        print("do get!")

    def POST(self):
        print("do post!")

    def HEAD(self):
        print("do head!")


class Request:
    def __init__(self, method):
        self.method = method


for ele in ("GET", "POST", "HEAD"):
    request = Request(ele)
    hs = HTTPHandler()
    hs.handle(request)
    del request
