import json
from config.redis import redis_client
from models.job import JOB_TYPE_TO_QUEUE, JobType

def add_job_to_queue(job_type: JobType, job: dict):
    queue_name = JOB_TYPE_TO_QUEUE[job_type]
    redis_client.lpush(queue_name, json.dumps(job))
    print(f"job added: {job['job_id']}")
    print(f"queue: {queue_name}")

def get_job_from_queue(job_type: JobType):
    queue_name = JOB_TYPE_TO_QUEUE[job_type]
    _, job_data = redis_client.brpop(queue_name)

    job = json.loads(job_data)

    print(f"job pooped: {job['job_id']}")
    print(f"queue: {queue_name}")
    return job

def clear_queue(job_type: JobType):
    queue_name = JOB_TYPE_TO_QUEUE[job_type]
    redis_client.delete(queue_name)

# def retry_job():
