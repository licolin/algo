# -*- encoding: utf-8 -*-
# Author: li_colin

class BaseExec:
    def __init__(self):
        pass

    @staticmethod
    def execNormal():
        print("execNormal")

    @staticmethod
    def execOther():
        print("execOther")


class CashBusiness(BaseExec):
    def __init__(self):
        super().__init__()

    @staticmethod
    def execNormal():
        print("CashBusiness execNormal")

    def dispatch(self):
        return {"normal": self.execNormal, "other": self.execOther}
