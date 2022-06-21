# -*- encoding: utf-8 -*-
# Author: li_colin
from base_sql import Mysql

mysql_trade = Mysql(host="10.25.24.207", user="mc-test", port=3306, password="mc-test", database="xtp_lzh")
mysql_trade.Connect()

mysql_case = Mysql(host="10.25.24.207", user="mc-test", port=3306, password="mc-test", database="xtp_lzh_test")
mysql_case.Connect()


def get_fee_info() -> dict:
    ret = mysql_trade.Select(
        "select t.fee_rate_name,t.value_max from xtp_fee_rate_define t where t.fee_rate_id in (1001,1002,1003,1004);")
    return {k: v if not isinstance(v, str) else float(v) for k, v in dict(ret).items()}


def get_user():
    ret = mysql_case.Select("select * from t_user")
    print(ret)
