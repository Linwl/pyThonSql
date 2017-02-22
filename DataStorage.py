#!/usr/bin/env python
# coding=utf-8

import pymssql

class DbHelper:
    """
       对pymssql的简单封装
       pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
       使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

       用法：

       """
    #初始化函数
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    #获取数据库连接信息
    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        try:
            self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,charset="utf8")
        except Exception, e:
            print '数据库连接错误:\t', e.message
        cur = self.conn.cursor()
        if not cur:
            raise ("连接数据库失败!")
        else:
            return  cur

    #执行查询函数
    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        data = cur.fetchall()  # 一次获取全部数据
        row = cur.fetchone()  # 一次获取一行数据
        rows = cur.fetchmany(10)  # 获取10行数据
        #查询完毕后必须关闭连接
        self.conn.close()
        return data

    #执行非查询语句
    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
    ss = DbHelper(host="61.142.204.26:1433", user="sa", pwd="hodi", db="Epcloud")
    data = ss.ExecQuery("Select * From Park")
    for row in data:
        print "parkid","物业编号"
        print row[0], row[1].encode("utf8")

if __name__ == '__main__':
    main()