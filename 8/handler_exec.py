# -*- encoding: utf-8 -*-
# Author: li_colin
from objprint import op
from handler_asset import AssetCheck
from handler_position import PositionCheck
from loguru import logger


class ExecAction:
    def handle(self, request, method):
        getattr(self, method)(request)

    @staticmethod
    def insertOrder(request):
        xtp_id = request.getApi().InsertOrder(request.order, request.getSession())
        request.setXtpID(xtp_id)
        request.setPreXtpId(xtp_id)

    @staticmethod
    def cancelOrder(request):
        xtp_id = request.getApi().CancelOrder(request.getPreXtpId(), request.getSession())
        request.setXtpID(xtp_id)
        request.setPreXtpId(xtp_id)

    @staticmethod
    def queryAsset(request):
        request.getApi().queryAsset(request.getSession())

    @staticmethod
    def queryPosition(request):
        request.getApi().queryPosition(request.getQueryPositionParams(), request.getSession())

    @staticmethod
    def Login(request):
        if request.userLoginAlready(request.getCurrentUserName()):
            request.setSession(request.getAlreadyLoginSession(request.getCurrentUserName()))
        else:
            request.getApi().SetSoftwareKey(request.getUserKey())
            session_id = request.getApi().Login(request.getUserInfo())
            if session_id:
                request.setSession(session_id)
                request.updateMapUserSession(request.getCurrentUserName(), session_id)
            else:
                request.setError(request.getApi().getApiLastError())
                request.setFlag(False)

    @staticmethod
    def Logout(request):
        if request.userLoginAlready(request.getCurrentUserName()):
            ret = request.getApi().Logout(request.getSessionFromMapUserSession(request.getCurrentUserName()))
            if ret == 0:
                request.deleteUserSession(request.getCurrentUserName())
                logger.info("delete user:{0} and session:{1} from user_session_map".format(request.getCurrentUserName,
                                                                                           request.getSession()))
            else:
                logger.error("user:{0} logout failed!".format(request.getCurrentUserName()))
        else:
            logger.warning("user:{0} state is not un-login".format(request.getCurrentUserName()))

    @staticmethod
    def WaitAll(request):
        import time
        end = time.time() + request.getTimeOut()
        while True:
            if request.getPreAsset() is not None and request.getPrePosition() is not None:
                logger.info("query pre asset and pre position success")
                break
            elif time.time() > end:
                request.setFlag(False)
                request.setExceptionInfo("PRE query position or query asset time out!")
                break
            else:
                pass

    @staticmethod
    def WaitPosition(request):
        import time
        end = time.time() + request.getTimeOut()
        while True:
            if request.getPrePosition() is not None:
                logger.info("query pre position success!")
                break
            elif time.time() > end:
                request.setFlag(False)
                request.setExceptionInfo("PRE query position time out!")
                break
            else:
                pass

    @staticmethod
    def WaitAsset(request):
        import time
        end = time.time() + request.getTimeOut()
        while True:
            if request.getPreAsset() is not None:
                logger.info("query pre asset success!")
                break
            elif time.time() > end:
                request.setFlag(False)
                request.setExceptionInfo("PRE query asset time out!")
                break
            else:
                pass

    @staticmethod
    def WaitAllLater(request):
        import time
        end = time.time() + request.getTimeOut()
        while True:
            if request.getAftAsset() is not None and request.getAftPosition() is not None:
                logger.info("get atf asset and position success!")
                break
            elif time.time() > end:
                request.setFlag(False)
                request.setExceptionInfo("AFT query asset or query position time out!")
                break
            else:
                pass

    @staticmethod
    def WaitOrderRtn(request):
        import time
        end = time.time() + request.getTimeOut()
        while True:
            if request.getOrderRtn() is not None:
                logger.info("order rtn success!")
                break
            elif time.time() > end:
                request.setFlag(False)
                request.setExceptionInfo("get order return time out!")
                break
            else:
                pass


class CashExecAction(ExecAction):
    @staticmethod
    def newInsertOrder(request):
        request.setXtpID(2)
        print(f"newInsertOrder!")


class PositionAssetCheck(PositionCheck, AssetCheck):
    pass


class CashExecAssetPosition(CashExecAction, PositionAssetCheck):
    pass


class Request:
    def __init__(self):
        self.map_user_session = {}
        self.TimeOut = None
        self.preXtpId = None
        self.xtpId = None
        self.pre_asset = None
        self.aft_asset = None
        self.pre_position = None
        self.atf_position = None
        self.error = None
        self.trade = None
        self.orderRtn = None
        self.user_info = None
        self.order = None
        self.session = None
        self.api = None
        self.flag = True
        self.ExceptionInfo = None
        self.expect_info = None
        self.case_info = None

    def setFlag(self, val: True | False):
        self.flag = val

    def setExceptionInfo(self, info: str):
        self.ExceptionInfo = info

    def getExceptionInfo(self):
        return self.ExceptionInfo

    def userLoginAlready(self, name):
        return name in self.map_user_session

    def getAlreadyLoginSession(self, name):
        return self.map_user_session[name]

    def getUserKey(self):
        if self.user_info is not None:
            return self.user_info["key"]

    def updateMapUserSession(self, name, session):
        if name not in self.map_user_session:
            self.map_user_session[name] = session

    def deleteUserSession(self, name):
        self.map_user_session.pop(name)

    def getSessionFromMapUserSession(self, name):
        return self.map_user_session[name]

    def getQueryPositionParams(self):
        return {"market": self.order["market"], "ticker": self.order["ticker"]}

    def setTimeOut(self, t):
        self.TimeOut = t

    def getTimeOut(self):
        return self.TimeOut

    def setPreAsset(self, asset):
        self.pre_asset = asset

    def setAftAsset(self, asset):
        self.aft_asset = asset

    def setPrePosition(self, position):
        self.pre_position = position

    def setAftPosition(self, position):
        self.atf_position = position

    def setError(self, error):
        self.error = error

    def setTrade(self, trade):
        self.trade = trade

    def setOrderRtn(self, order):
        self.orderRtn = order

    def setXtpID(self, id):
        self.xtpId = id

    def setPreXtpId(self, id):
        self.preXtpId = id

    def getXtpID(self):
        return self.xtpId

    def getPreXtpId(self):
        return self.preXtpId

    def getPreAsset(self):
        return self.pre_asset

    def getPrePosition(self):
        return self.pre_position

    def getAftAsset(self):
        return self.aft_asset

    def getAftPosition(self):
        return self.atf_position

    def getOrderRtn(self):
        return self.orderRtn

    def getOrder(self):
        return self.order

    def setOrder(self, order):
        self.order = order

    def getSession(self):
        return self.session

    def setSession(self, session):
        self.session = session

    def setApi(self, api):
        self.api = api

    def getApi(self):
        return self.api

    def getUserInfo(self):
        return self.user_info

    def setUserInfo(self, user):
        self.user_info = user

    def getCurrentUserName(self):
        return self.getUserInfo()["user"] if self.getUserInfo() else None

    def setExpectInfo(self, info: dict) -> None:
        self.expect_info = info

    def getExpectInfo(self) -> dict:
        return self.expect_info

    def getCaseInfo(self) -> dict:
        return self.case_info if self.case_info is not None else {}

    def setCaseInfo(self, val: dict) -> None:
        self.case_info = val

    def setInit(self):
        self.expect_info = None
        self.xtpId = None
        self.pre_asset = None
        self.aft_asset = None
        self.pre_position = None
        self.atf_position = None
        self.error = None
        self.trade = None
        self.orderRtn = None
        self.user_info = None
        self.order = None
        self.session = None
        self.case_info = None


req = Request()
ex = CashExecAssetPosition()
