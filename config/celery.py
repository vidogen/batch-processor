from celery import Celery
from kombu import Queue
from config.constants import BROKER, BACKEND_CELERY
from models.job import JOB_TYPE_TO_QUEUE


celery = Celery(
    "batch_processor",
    broker=BROKER,
    backend=BACKEND_CELERY
)

celery.conf.task_queues = [
    Queue(
        name=queue_name,
        routing_key=queue_name
    )
    for queue_name in JOB_TYPE_TO_QUEUE.values()
]

celery.conf.task_default_exchange = "default"
celery.conf.task_default_exchange_type = "direct"

import core.worker