from celery import Celery

broker_url = 'amqp://defaultuser:defaultpassword@localhost/'

app = Celery('tasks', backend='rpc', broker=broker_url)

@app.task
def add(x, y):
    return x + y
