# -*- encoding: utf-8 -*-
# Author: li_colin
from parms import BusinessType, Market, Side, PriceType, PositionEffect
from base_queue import Queue
from test_sql import get_fee_info
import sys


# user_info = {"ip": "10.25.24.233", "port": 8002, "sock_type": 1, "user": "2110019982", "password": "123456",
#              "local_ip": "10.25.102.41", "auto_login": True, "key": "f11dcc367a5963df20be15408df9a86c"}
# expect_info = {
#     "error_code": 11110001,
#     "error_msg": "msg",
#     "expect_status": 0
# }
# case_info = {
#     "id": 1,
#     "desc": "stock buy all-trade"
# }
#
# order_info = {
#     'business_type': BusinessType.XTP_BUSINESS_TYPE_CASH,
#     'order_client_id': 2,
#     'market': Market.XTP_MKT_SZ_A,
#     'ticker': '000001',
#     'side': Side.XTP_SIDE_BUY,
#     'price_type': PriceType.XTP_PRICE_LIMIT,
#     'price': 20,
#     'quantity': 200,
#     'position_effect': PositionEffect.XTP_POSITION_EFFECT_OPEN
# }
#
# operations = ["Login", "queryAsset", "queryPosition", "WaitAll", "insertOrder", "WaitOrderRtn", "queryAsset",
#               "queryPosition", "WaitAllLater", "AssetAllTrade", "PositionAllTrade"]
#
# user_info1 = {"ip": "10.25.24.233", "port": 8002, "sock_type": 1, "user": "53120023676", "password": "123456",
#               "local_ip": "10.25.102.41", "auto_login": True, "key": "f11dcc367a5963df20be15408df9a86c"}
# expect_info1 = {
#     "error_code": 11110001,
#     "error_msg": "msg",
#     "expect_status": 0
# }
# case_info1 = {
#     "id": 2,
#     "desc": "stock sell all-trade"
# }
#
# order_info1 = {
#     'business_type': BusinessType.XTP_BUSINESS_TYPE_CASH,
#     'order_client_id': 3,
#     'market': Market.XTP_MKT_SZ_A,
#     'ticker': '000001',
#     'side': Side.XTP_SIDE_BUY,
#     'price_type': PriceType.XTP_PRICE_LIMIT,
#     'price': 20,
#     'quantity': 100,
#     'position_effect': PositionEffect.XTP_POSITION_EFFECT_OPEN
# }
#
# operations1 = ["Login", "queryAsset", "queryPosition", "WaitAll", "insertOrder", "WaitOrderRtn", "queryAsset",
#                "queryPosition", "WaitAllLater", "AssetAllTrade", "PositionAllTrade"]


class InputParams:
    def __init__(self):
        self._user_info = None
        self._expect_info = None
        self._order_info = None
        self._operations = None
        self._fee_ratio = None
        self._case_info = None

    @property
    def user_info(self):
        return self._user_info

    @user_info.setter
    def user_info(self, val):
        self._user_info = val

    @property
    def expect_info(self):
        return self._expect_info

    @expect_info.setter
    def expect_info(self, val):
        self._expect_info = val

    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, val):
        self._order_info = val

    @property
    def operations(self):
        return self._operations

    @operations.setter
    def operations(self, val: list) -> None:
        self._operations = val

    @property
    def fee_ratio(self):
        return self._fee_ratio

    @fee_ratio.setter
    def fee_ratio(self, val):
        self._fee_ratio = val

    @property
    def case_info(self):
        return self._case_info

    @case_info.setter
    def case_info(self, val):
        self._case_info = val


iq = Queue()
