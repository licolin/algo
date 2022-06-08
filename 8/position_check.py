# -*- encoding: utf-8 -*-
# Author: li_colin

class PositionCheck:
    def handle(self, request):
        method_name = request.method
        print(getattr(self, method_name))
        getattr(self, method_name)(request)

    @staticmethod
    def AllTrade(request):
        print("AllTrade!")

    @staticmethod
    def HalfTrade(request):
        print("HalfTrade")

    @staticmethod
    def Cancel(request):
        print("insertOrder")

    @staticmethod
    def CancelError(request):
        print("CancelError!")
