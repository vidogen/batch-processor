import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

CHAR_SHEET_IMG_QUEUE = "character_sheet_img_gen_queue"