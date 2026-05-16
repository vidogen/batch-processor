from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class JobStatus(str, Enum):
    IDLE = "idle"
    STARTED = "started"
    IN_PROGRESS = "in progress"
    SUCCESS = "success"
    FAILED = "failed"

class Job(BaseModel):
    job_id: str
    job_status: JobStatus = Field(default=JobStatus.IDLE)
    json_content: str

    retries: int = 0
    max_retries: int = 3

    job_started_at: datetime

