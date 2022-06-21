# -*- encoding: utf-8 -*-
# Author: li_colin
from loguru import logger
from xapi import api
from handler_exec import req, ex
from objprint import op
from handler_data import iq

if __name__ == "__main__":
    logger.add("test_{time}.log", format="{name} {message}", level="DEBUG", rotation="08:00")
    req.setApi(api)
    req.setTimeOut(3)
    logger.info("async wait time-out is ", req.getTimeOut())
    while iq.qsize() > 0:
        input_info = iq.get()
        req.setInit()
        req.setCaseInfo(input_info.case_info)
        req.setOrder(input_info.order_info)
        req.setUserInfo(input_info.user_info)
        req.setExpectInfo(input_info.expect_info)
        for ele in input_info.operations:
            if req.flag:
                ex.handle(req, ele)
            else:
                logger.error(
                    "{0} {1} {2}".format(input_info.case_info["id"], input_info.case_info["desc"],
                                         req.getExceptionInfo()))