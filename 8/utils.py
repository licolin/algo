from loguru import logger


def init_trading_info(info):
    """
    XTP_ORDER_SUBMIT_STATUS_INSERT_SUBMITTED = 1, ///<订单已经提交
    XTP_ORDER_SUBMIT_STATUS_INSERT_ACCEPTED,///<订单已经被接受
    XTP_ORDER_SUBMIT_STATUS_INSERT_REJECTED,///<订单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_SUBMITTED,///<撤单已经提交
    XTP_ORDER_SUBMIT_STATUS_CANCEL_REJECTED,///<撤单已经被拒绝
    XTP_ORDER_SUBMIT_STATUS_CANCEL_ACCEPTED ///<撤单已经被接受
    """
    if type(info) == dict and info:
        for e in info:
            if str(info[e]) not in globals.user_trading_info:
                globals.user_trading_info[str(info[e])] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"]["Rtn_Ack"] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"]["Rtn_Rej"] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"]["Rtn_Ack_Cancel"] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"]["Rtn_Rej_Cancel"] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"]["Rtn_Error"] = dict()
                globals.user_trading_info[str(info[e])]["Rtn"]["Cancel_Error"] = dict()
                globals.user_trading_info[str(info[e])]["Trd"] = dict()
                globals.user_trading_info[str(info[e])]["Trd"]["trd_1"] = dict()
                globals.user_trading_info[str(info[e])]["Trd"]["trd_2"] = dict()
                globals.user_trading_info[str(info[e])]["PreAsset"] = dict()
                globals.user_trading_info[str(info[e])]["AftAsset"] = dict()
                globals.user_trading_info[str(info[e])]["PrePosition"] = dict()
                globals.user_trading_info[str(info[e])]["AftPosition"] = dict()
            else:
                logger.warning("{} init trading data already exists!".format(str(info[e])))
    elif type(info) == list and info:
        for e in info:
            if str(e) not in globals.user_trading_info:
                globals.user_trading_info[str(e)] = dict()
                globals.user_trading_info[str(e)]["Rtn"] = dict()
                globals.user_trading_info[str(e)]["Rtn"]["Rtn_Ack"] = dict()
                globals.user_trading_info[str(e)]["Rtn"]["Rtn_Rej"] = dict()
                globals.user_trading_info[str(e)]["Rtn"]["Rtn_Ack_Cancel"] = dict()
                globals.user_trading_info[str(e)]["Rtn"]["Rtn_Rej_Cancel"] = dict()
                globals.user_trading_info[str(e)]["Rtn"]["Rtn_Error"] = dict()
                globals.user_trading_info[str(e)]["Rtn"]["Cancel_Error"] = dict()
                globals.user_trading_info[str(e)]["Trd"] = dict()
                globals.user_trading_info[str(e)]["Trd"]["trd_1"] = dict()
                globals.user_trading_info[str(e)]["Trd"]["trd_2"] = dict()
                globals.user_trading_info[str(e)]["PreAsset"] = dict()
                globals.user_trading_info[str(e)]["AftAsset"] = dict()
                globals.user_trading_info[str(e)]["PrePosition"] = dict()
                globals.user_trading_info[str(e)]["AftPosition"] = dict()
            else:
                logger.warning("{} init trading data already exists!".format(str(e)))
    else:
        logger.warning("info type is {},wrong type or is null!".format(type(info)))
