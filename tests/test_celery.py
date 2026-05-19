from datetime import datetime
import uuid
from celery import Task

from core.job_queue import clear_queue
from models.job import JOB_TYPE_TO_QUEUE, Job, JobStatus, JobType
from core.worker import process_job

process_job: Task

def test_send_jobs(n=100):
    
    for i in range(n):
        job = Job(
            job_id = str(uuid.uuid4()),
            job_type = JobType.CHAR_SHEET,
            json_content = "{}",
            job_status = JobStatus.STARTED,
            job_started_at= datetime.now()
        )

        queue_name = JOB_TYPE_TO_QUEUE[JobType.CHAR_SHEET]

        process_job.apply_async(
            args=[job.model_dump(mode="json")],
            queue=queue_name,
            routing_key=queue_name
        )

        print(f"sent job: {job.job_id} --> {queue_name}")


test_send_jobs(100)