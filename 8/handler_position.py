# -*- encoding: utf-8 -*-
# Author: li_colin

class PositionCheck:
    def handle(self, request, method):
        getattr(self, method)(request)

    @staticmethod
    def PositionAllTrade(request):
        print("Position AllTrade!")

    @staticmethod
    def PositionHalfTrade(request):
        print("Position HalfTrade")

    @staticmethod
    def PositionCancel(request):
        print("Position insertOrder")

    @staticmethod
    def PositionCancelError(request):
        print("Position CancelError!")
