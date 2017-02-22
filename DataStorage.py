#!/usr/bin/env python
# coding=utf-8

import pymssql

class SqlServer:
    """
       对pymssql的简单封装
       pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
       使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

       用法：

       """

    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def _GetConnect(self):
        """
         得到连接信息
         返回: conn.cursor()
        """
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise ("连接数据库失败!")
