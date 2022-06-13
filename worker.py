import os

import redis
from rq import Worker, Queue, Connection

listen = ['default']

# r = redis.Redis()
redis_url = os.getenv('REDIS_URL')

r = redis.from_url(redis_url)

q = Queue(connection=r)
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
        
