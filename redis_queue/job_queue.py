import json
from config.redis import redis_client
from constants import CHAR_SHEET_IMG_QUEUE

def add_job_to_queue(job):
    redis_client.lpush(CHAR_SHEET_IMG_QUEUE, json.dumps(job))
    print(f"job added: {job['job_id']}")

def get_job_from_queue():
    _, job_data = redis_client.brpop(CHAR_SHEET_IMG_QUEUE)

    job = json.loads(job_data)

    print(f"job popped: {job['job_id']}")
    return job

def clear_queue():
    redis_client.delete(CHAR_SHEET_IMG_QUEUE)

# def retry_job():
