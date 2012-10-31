#coding:utf-8

import _env
from config import redis, redis_key
from os import urandom
from struct import pack, unpack
from base64 import urlsafe_b64encode, urlsafe_b64decode
import binascii

REDIS_SESSION = redis_key.Session()

# 常量
class Session(object):
    @staticmethod
    def get(id):
        return redis.hget(REDIS_SESSION, id)

    @staticmethod
    def set(id, value):
        if value: 
            redis.hset(REDIS_SESSION, id, value)
        else:
            redis.hdel(REDIS_SESSION, id)


# 接口
############################################
def session_new(id):
    s = Session.get(id)
    if not s:
        s = urandom(12)
        Session.set(id, s)
    return _id_binary_encode(id, s)

def id_by_session(session):
    if session:
        id, binary = _id_binary_decode(session)
        if id and binary and binary == Session.get(id):
            return id

def session_rm(id):
    Session.set(id, None)


# 内部函数
############################################

def _id_by_base64(string):
    try:
        id = urlsafe_b64decode(string+'==')
    except (binascii.Error, TypeError):
        return 0
    else:
        return unpack('Q', id)[0]

def _id_binary_decode(session):
    if not session:
        return None, None
    id = session[:11]
    value = session[11:]
    try:
        value = urlsafe_b64decode(value+'=')
    except (binascii.Error, TypeError):
        return None, None
    id = _id_by_base64(id)
    return id, value

def _id_binary_encode(id, session):
    id_key = pack('Q', int(id))
    id_key = urlsafe_b64encode(id_key).rstrip('=')
    ck_key = urlsafe_b64encode(session)
    return '%s%s'%(id_key, ck_key)


if __name__ == '__main__':
    print session_new(12345)
