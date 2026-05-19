from datetime import datetime
import uuid

from models.job import Job, JobStatus
from core.worker import process_job


def send_jobs(n=100):
    for i in range(n):
        job = Job(
            job_id = str(uuid.uuid4()),
            json_content = "{}",
            job_status = JobStatus.STARTED,
            job_started_at= datetime.now()
        )

        process_job.delay(job.model_dump(mode="json"))


send_jobs(100)