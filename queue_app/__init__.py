from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)

from queue_app import views
from queue_app import tasks