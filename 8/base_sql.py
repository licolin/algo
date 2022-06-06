# -*- encoding: utf-8 -*-
# Author: li_colin

import pymysql as pys
from loguru import logger


class Mysql:
    def __init__(self, host, user, port, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.port = port
        self.database = database
        self.password = password
        self.session = None
        self.conn = None

    def Connect(self):
        self.conn = pys.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                port=3306)
        self.session = self.conn.cursor()

    def Close(self):
        if self.session is not None:
            self.session.close()
        if self.conn is not None:
            self.conn.close()
        self.session = None
        self.conn = None

    def Select(self, sql):
        logger.info(sql)
        try:
            if self.session and self.conn:
                self.session.execute(sql)
                ret = self.session.fetchall()
                return ret if ret else None
            else:
                logger.error("connect mysql error")
        except Exception as e:
            logger.exception(e)

    def UpdateInsertDelete(self, sql, operation=None):
        logger.info(sql)
        try:
            if self.session and self.conn:
                self.session.execute(sql)
            else:
                logger.error(f"operation {operation},connect mysql error")
        except Exception as e:
            logger.exception(e)
