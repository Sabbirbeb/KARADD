import redis
from globals import REDIS_QUEUE_NAME

class Redis:
    '''
    Class for contributing with REDIS
    '''
    def __init__(self, host:(str)='localhost', port:(str|int)=6379):
        '''
        Initializing object for REDIS
        '''
        self._host = host
        self._port = port
        self.conn = redis.Redis(host=self._host, port=self._port, db=0)

    # by keys
    def get_by_key(self, key:(str|int)):
        '''
        Get item from REDIS by the key
        '''
        binary = self.conn.get(key)
        return binary.decode('UTF-8')

    def set_by_key(self, key:(str|int), value):
        '''
        Set item to REDIS by the key
        '''
        res_code = self.conn.set(key, value)
        return res_code

    # queues
    def rpush_queue(self, queue_name:str = REDIS_QUEUE_NAME, value = ''):
        '''
        Rpush value to REDIS queue  
        '''
        res_code = self.conn.rpush(queue_name, value)
        return res_code

    def lpop_queue(self, queue_name:str = REDIS_QUEUE_NAME):
        '''
        Lpop value from REDIS queue
        '''
        binary = self.conn.lpop(queue_name)
        return binary.decode('UTF-8')
    
    def llen_queue(self, queue_name:str = REDIS_QUEUE_NAME):
        '''
        Llen of queue in REDIS
        '''
        length = self.conn.llen(queue_name)
        return length
