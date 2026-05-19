from celery import Celery
from config.constants import CHAR_SHEET_IMG_QUEUE, BROKER, BACKEND_CELERY

celery = Celery(
    CHAR_SHEET_IMG_QUEUE,
    broker=BROKER,
    backend=BACKEND_CELERY
)

import workers.worker