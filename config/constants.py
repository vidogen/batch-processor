import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

CHAR_SHEET_IMG_QUEUE = "character_sheet_generation_queue"
CHARACTER_JSON_QUEUE = "character_json_generation_queue"
EPISODE_JSON_QUEUE = "episode_json_generation_queue"
SCENE_JSON_QUEUE = "scene_json_generation_queue"
BG_AUDIO_QUEUE = "background_audio_generation_queue"
DIALOG_AUDIO_QUEUE = "dialog_audio_generation_queue"
FAILED_JOBS_QUEUE = "failed_jobs_queue"
RETRY_QUEUE = "retry_jobs_queue"

BROKER = f"redis://{REDIS_HOST}:{REDIS_PORT}/0" # queue storing jobs
BACKEND_CELERY = f"redis://{REDIS_HOST}:{REDIS_PORT}/1" # stores result of the worker 


if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env or export it in terminal.")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Add it to your .env or export it in terminal.")