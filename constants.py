import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

CHAR_SHEET_IMG_QUEUE = "character_sheet_img_gen_queue"

BROKER = f"redis://{REDIS_HOST}:{REDIS_PORT}/0" #queue storing jobs
BACKEND_CELERY = f"redis://{REDIS_HOST}:{REDIS_PORT}/1" #stores result of the worker 