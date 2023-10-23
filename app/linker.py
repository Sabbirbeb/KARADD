import redis

def get_next(key, index: int):
    key = list(key)
    if ord(key[index]) == 122:
        key[index] = 'a'
        if index != 0 and abs(index) != len(key):
            key = get_next(key, index-1)
    else:
        key[index] = chr(ord(key[index]) + 1)
    return ''.join(key)

async def get_link_from_redis(key=None):
    if key and key != 'key':
        try:
            red = redis.Redis(host='localhost', port=6379)
            queue = red.keys()
            for i in queue:
                if i.decode("utf-8") == key:
                    ret = red.get(key).decode("utf-8")
                    break
            else:
                ret = "https://www.ya.ru/"
        except:
            ret = "https://www.ya.ru/"
    else:
        ret = "https://www.ya.ru/"
    return ret

        

async def set_link_from_redis(value=None):
    if value:
        try:
            red = redis.Redis(host='localhost', port=6379)
            key = red.get('key').decode("utf-8") 
            key = get_next(key, -1)
            red.set('key', key)
            red.set(key, value)
            return key
        except Exception as e:
            return None