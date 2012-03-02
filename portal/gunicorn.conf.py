import os
import multiprocessing

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

workers = multiprocessing.cpu_count() * 2 + 1
worker_connections = 2048

daemon = False
timeout = 90

user = 'pugpe'
group = 'pugpe'

pidfile = os.path.join(PROJECT_ROOT, 'gunicorn.pid')
accesslog = os.path.join(PROJECT_ROOT, 'logs/access_gunicorn.log')
errorlog = os.path.join(PROJECT_ROOT, 'logs/error_gunicorn.log')

loglevel = 'info'
