from time import sleep
from config.celery import celery
from models.job import Job, JobStatus
from celery.app.task import Task

@celery.task(bind=True, max_retries=3)
def process_job(self: Task, job: dict):
    try:
        print(f"job started processing: {job['job_id']}")

        # start job
        print(f"START {job['job_id']}")

        # simulating heavy time taking work here
        print("doing heavy work...")
        job["job_status"] = JobStatus.IN_PROGRESS
        sleep(3)

        # job success
        job["job_status"] = JobStatus.SUCCESS
        print(f"END {job['job_id']}")

        return {
            "success": True,
            "status": f"job id: {job['job_id']} processed successfully"
        }

    except Exception as e:
        print(e)
        print(f"retry count: {self.request.retries}/{self.max_retries}")
        raise self.retry(exc=e, countdown=5)

