# -*- encoding: utf-8 -*-
# Author: li_colin
from enum import IntEnum


class BusinessType(IntEnum):
    # 普通股票业务（股票买卖，ETF买卖，沪市交易型货币基金等）
    XTP_BUSINESS_TYPE_CASH = 0
    # 新股申购业务（对应的price type需选择限价类型）
    XTP_BUSINESS_TYPE_IPOS = 1
    # 回购业务（国债逆回购业务对应的price type填为限价，side填为卖）
    XTP_BUSINESS_TYPE_REPO = 2,
    # ETF申赎业务
    XTP_BUSINESS_TYPE_ETF = 3
    # 融资融券业务
    XTP_BUSINESS_TYPE_MARGIN = 4
    # 转托管（未支持）
    XTP_BUSINESS_TYPE_DESIGNATION = 5
    # 配股业务（对应的price type需选择限价类型, side填为买）
    XTP_BUSINESS_TYPE_ALLOTMENT = 6
    # 分级基金申赎业务
    XTP_BUSINESS_TYPE_STRUCTURED_FUND_PURCHASE_REDEMPTION = 7
    # 分级基金拆分合并业务
    XTP_BUSINESS_TYPE_STRUCTURED_FUND_SPLIT_MERGE = 8
    # < 货币基金申赎业务（暂未支持，沪市交易型货币基金的买卖请使用普通股票业务）
    XTP_BUSINESS_TYPE_MONEY_FUND = 9
    # 期权业务
    XTP_BUSINESS_TYPE_OPTION = 10
    # 行权
    XTP_BUSINESS_TYPE_EXECUTE = 11
    # 锁定解锁，暂不支持
    XTP_BUSINESS_TYPE_FREEZE = 12
    # 13
    XTP_BUSINESS_TYPE_OPTION_COMBINE = 13
    # 组合和拆分业务
    XTP_BUSINESS_TYPE_EXECUTE_COMBINE = 14
    XTP_BUSINESS_TYPE_UNKNOWN = 15


class Market(IntEnum):
    XTP_MKT_INIT = 0
    XTP_MKT_SZ_A = 1
    XTP_MKT_SH_A = 2


class Side(IntEnum):
    XTP_SIDE_BUY = 1
    XTP_SIDE_SELL = 2
    XTP_SIDE_PURCHASE = 7
    XTP_SIDE_REDEMPTION = 8
    XTP_SIDE_SPLIT = 9
    XTP_SIDE_MERGE = 10
    XTP_SIDE_COVER = 11
    XTP_SIDE_FREEZE = 12
    XTP_SIDE_MARGIN_TRADE = 21
    XTP_SIDE_SHORT_SELL = 22
    XTP_SIDE_REPAY_MARGIN = 23
    XTP_SIDE_REPAY_STOCK = 24
    XTP_SIDE_CASH_REPAY_MARGIN = 25
    XTP_SIDE_STOCK_REPAY_STOCK = 26
    XTP_SIDE_UNKNOWN = 27


class PriceType(IntEnum):
    # < 限价单 - 沪 / 深 / 沪期权 / 深期权 （除普通股票业务外，其余未特指的业务均使用此种类型）
    XTP_PRICE_LIMIT = 1
    # // / < 即时成交剩余转撤销，市价单 - 深 / 沪期权 / 深期权
    XTP_PRICE_BEST_OR_CANCEL = 2
    # // / < 最优五档即时成交剩余转限价，市价单 - 沪
    XTP_PRICE_BEST5_OR_LIMIT = 3
    # // / < 最优5档即时成交剩余转撤销，市价单 - 沪深 / 深期权
    XTP_PRICE_BEST5_OR_CANCEL = 4
    # < 全部成交或撤销, 市价单 - 深 / 沪期权 / 深期权
    XTP_PRICE_ALL_OR_CANCEL = 5
    # // / < 本方最优，市价单 - 深 / 深期权 / 沪科创板
    XTP_PRICE_FORWARD_BEST = 6
    # // / < 对方最优剩余转限价，市价单 - 深 / 沪期权 / 深期权 / 沪科创板
    XTP_PRICE_REVERSE_BEST_LIMIT = 7
    # // / < 期权限价申报FOK
    XTP_PRICE_LIMIT_OR_CANCEL = 8
    #  // / < 未知或者无效价格类型
    XTP_PRICE_TYPE_UNKNOWN = 9


class PositionEffect(IntEnum):
    XTP_POSITION_EFFECT_INIT = 0
    # 开
    XTP_POSITION_EFFECT_OPEN = 1
    # 平
    XTP_POSITION_EFFECT_CLOSE = 2
    # 强平
    XTP_POSITION_EFFECT_FORCECLOSE = 3
    # 平今
    XTP_POSITION_EFFECT_CLOSETODAY = 4
    # 平昨
    XTP_POSITION_EFFECT_CLOSEYESTERDAY = 5
    # 强减
    XTP_POSITION_EFFECT_FORCEOFF = 6
    # 本地强平
    XTP_POSITION_EFFECT_LOCALFORCECLOSE = 7
    # 信用业务追保强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_COVER = 8
    # 信用业务清偿强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_CLEAR = 9
    # 信用业务合约到期强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_DEBT = 10
    # 信用业务无条件强平
    XTP_POSITION_EFFECT_CREDIT_FORCE_UNCOND = 11
    # 未知的开平标识类型
    XTP_POSITION_EFFECT_UNKNOWN = 12
