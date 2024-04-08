# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import json
    import redis
    class foo():
        def __init__(self):
            pass
        def fun(self):
            return None
    r = redis.StrictRedis(host='localhost', port=6379)
    r.hset('ai service', 'modelname', json.dumps(foo))
    r.hset('ai service', 'modelname', 'model2')
    res = r.hget('ai service', 'modelname')
    print(res)
