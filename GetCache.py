#!/usr/bin/env python
# coding=utf-8

import redis

class RedisHelper:
    '''
    获取redis里面的缓存日常电量数据
    '''

    # 模块版本号
    _Version ="1.0.2017222"

    # 初始化函数
    def __init__(self, host,port ):
        self.host = "61.142.204.26"
        self.port = "6602"


    # 连接redis缓存函数
    def __GetConnect(self):
        try:
            re = redis.Redis(host=self.host, port=self.port,db="0")
        except Exception, e:
            raise 'Redis连接错误:\t', e.message
        return re

    # 单条redis缓存
    def SetRedis(self,Key, Value):
        try:
            re = self.__GetConnect()
            re.set(Key, Value)
        except Exception, exception:
            print exception

    #根据Key获取单条缓存
    def GetRedis(self,Key):
        try:
           re = self.__GetConnect()
           return re.get(Key)
        except Exception, exception:
            print exception

    #获取redis缓存的记录数量
    def GetBbsiza(self):
        try:
            re = self.__GetConnect()
            return  re.dbsize()
        except Exception, exception:
            print exception

    # 批量设置redis缓存
    def MsetRedis(self, lst):
        try:
            re = self.__GetConnect()
            re.mset(lst)
        except Exception, exception:
            print exception

    #批量获取redis缓存
    def MgetRedis(self, keys):
        try:
            re = self.__GetConnect()
            return re.mget(keys)
        except Exception, exception:
            print exception

    #利用list设置redis缓存
    def SetLpush(self,lstName,values):
        try:
            re = self.__GetConnect()
            return re.lpush(lstName,values)
        except Exception, exception:
            print exception

    #清空缓存
    def clear(self):
        try:
            re = self.__GetConnect()
            return re.flushdb()
        except Exception, exception:
            print exception

def main():
    ss = RedisHelper(host="61.142.204.26",port="6602")
    print ss.GetBbsiza()
    # ss.clear()

if __name__ == '__main__':
    main()