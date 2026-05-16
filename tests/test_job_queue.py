import uuid
from redis_queue import add_job_to_queue, get_job_from_queue, clear_queue

def test_and_get_job():
    
    clear_queue()

    job = {
        "job_id": str(uuid.uuid4()),
        "type": "character sheet gen",
        "prompt": "generate a image of gon the stonage boy as his character sheet"
    }

    add_job_to_queue(job)
    pooped_job = get_job_from_queue()

    assert pooped_job["job_id"] == job["job_id"]
    assert pooped_job["type"] == job["type"]

