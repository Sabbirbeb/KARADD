import redis
import json

from globals import REDIS_QUEUE_NAME
from classes.redis import Redis

r = redis.Redis(host='localhost', port=6379, db=0)

#!# only get by there
r.set('foo', 'bar')

# True
print (r.get('foo').decode('UTF-8'))
# b'bar'

r.rpush(REDIS_QUEUE_NAME, "boba")
print (r.llen(REDIS_QUEUE_NAME))

while r.llen(REDIS_QUEUE_NAME):
    print(r.rpop(REDIS_QUEUE_NAME).decode('UTF-8'))

interface = Redis()
interface.rpush_queue(value='pups')

while interface.llen_queue():
    print (interface.lpop_queue())