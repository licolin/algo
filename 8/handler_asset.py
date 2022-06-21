# -*- encoding: utf-8 -*-
# Author: li_colin

class AssetCheck:
    def handle(self, request, method):
        getattr(self, method)(request)

    @staticmethod
    def AssetAllTrade(request):
        print("Asset AllTrade!")

    @staticmethod
    def AssetHalfTrade(request):
        print("Asset HalfTrade")

    @staticmethod
    def AssetCancel(request):
        print("Asset insertOrder")

    @staticmethod
    def AssetCancelError(request):
        print("Asset CancelError!")
