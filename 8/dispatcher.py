# -*- encoding: utf-8 -*-
# Author: li_colin

class HTTPHandler:
    def handle(self, request):
        methname = 'do_' + request.method
        getattr(self, methname)()

    def do_GET(self):
        print("do get!")

    def do_POST(self):
        print("do post!")

    def do_HEAD(self):
        print("do head!")


class Request:
    def __init__(self, method):
        self.method = method


for ele in ("GET", "POST", "HEAD"):
    request = Request(ele)
    hs = HTTPHandler()
    hs.handle(request)
    del request
