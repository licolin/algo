# -*- encoding: utf-8 -*-
# Author: li_colin
from handler_exec import req, CashExecAction

Ex = CashExecAction()
req.setOperation1("queryAsset")
req.setOperation2("queryPosition")
req.setOperation3("newInsertOrder")
req.setOperation4("queryAsset")
req.setOperation5("queryPosition")

if req.getOperation1():
    Ex.handle(req, req.getOperation1())
if req.getOperation2():
    Ex.handle(req, req.getOperation2())
if req.getOperation3():
    Ex.handle(req, req.getOperation3())
if req.getOperation4():
    Ex.handle(req, req.getOperation3())
if req.getOperation5():
    Ex.handle(req, req.getOperation3())
print(req.getXtpID())
