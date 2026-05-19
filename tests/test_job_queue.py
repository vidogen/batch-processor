from datetime import datetime
import json
import uuid
from models.job import Job, JobStatus, JobType
from core.job_queue import add_job_to_queue, get_job_from_queue, clear_queue

def test_and_get_job():
    
    clear_queue(JobType.CHAR_SHEET)

    with open("mock_char.json", "r") as f:
        jsonData = json.load(f) 

    json_str = json.dumps(jsonData) 

    job = Job(
        job_id= str(uuid.uuid4()),
        json_content=json_str,
        job_status=JobStatus.STARTED,
        job_started_at=datetime.now()
    )

    add_job_to_queue(JobType.CHAR_SHEET, job.model_dump(mode="json"))
    pooped_job = get_job_from_queue(JobType.CHAR_SHEET)

    expected = job.model_dump(mode="json")

    assert pooped_job["job_id"] == expected["job_id"]

