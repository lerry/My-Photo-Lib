#coding:utf-8
import uuid
from config import redis
from config import KEY_SESSION

def session_new(uid):
    s = str(uuid.uuid4()).replace('-', '')
    session_set(uid, s)
    return s

def session_get(s):
    return redis.hget(KEY_SESSION, s)

def session_set(uid, s):
    redis.hset(KEY_SESSION, s, uid)

def session_rm(s):
    redis.hdel(KEY_SESSION, s)
    Session.set(id, None)

def session_flush():
    redis.delete(KEY_SESSION)

if __name__ == '__main__':
    pass
    print session_new(10000)
