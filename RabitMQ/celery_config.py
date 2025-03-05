import os
import time

from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RabitMQ.settings')
app = Celery('RabitMQ')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


@app.task(queue='tasks')
def task_1(phone_number, message):
    print(phone_number, '<===>', message)
    time.sleep(3)
    return message + f' has been send to {phone_number}'


task_1.delay(phone_number='+91123456789', message='Task 1')

app.autodiscover_tasks()
