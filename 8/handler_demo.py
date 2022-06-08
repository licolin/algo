# -*- encoding: utf-8 -*-
# Author: li_colin

class ExecAction:
    def handle(self, request):
        method_name = request.method
        print(getattr(self, method_name))
        getattr(self, method_name)(request)

    @staticmethod
    def insertOrder(request):
        print("insertOrder!")

    @staticmethod
    def cancelOrder(request):
        print("insertOrder")

    @staticmethod
    def queryAsset(request):
        print("insertOrder")

    @staticmethod
    def queryPosition(request):
        print("queryPosition!")


class CashExecAction(ExecAction):
    @staticmethod
    def newInsertOrder(request):
        print(f"newInsertOrder! {request.method}")


class Request:
    def __init__(self, method):
        self.method = method
        self.pre_asset = None
        self.aft_asset = None
        self.pre_position = None
        self.atf_position = None


exec = CashExecAction()
request = Request("newInsertOrder")
exec.handle(request)
