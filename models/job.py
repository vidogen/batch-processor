from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from config.constants import CHAR_SHEET_IMG_QUEUE, CHARACTER_JSON_QUEUE, SCENE_JSON_QUEUE, EPISODE_JSON_QUEUE, BG_AUDIO_QUEUE, DIALOG_AUDIO_QUEUE

class JobStatus(str, Enum):
    IDLE = "idle"
    STARTED = "started"
    IN_PROGRESS = "in progress"
    SUCCESS = "success"
    FAILED = "failed"

class JobType(str, Enum):
    CHAR_SHEET = "character sheet generation"
    CHARACTER_JSON = "character json generation"
    EPISODE_JSON = "episode json generation"
    SCENE_JSON = "scene json generation"
    BG_AUDIO = "background audio mp3 generation"
    DIALOG_AUDIO = "dialog audio mp3 generation"

JOB_TYPE_TO_QUEUE = {
    JobType.CHAR_SHEET: CHAR_SHEET_IMG_QUEUE,
    JobType.CHARACTER_JSON: CHARACTER_JSON_QUEUE,
    JobType.EPISODE_JSON: EPISODE_JSON_QUEUE,
    JobType.SCENE_JSON: SCENE_JSON_QUEUE,
    JobType.BG_AUDIO: BG_AUDIO_QUEUE,
    JobType.DIALOG_AUDIO: DIALOG_AUDIO_QUEUE,
}

class Job(BaseModel):
    job_id: str
    job_type: JobType = Field(default=JobType.CHAR_SHEET)
    job_status: JobStatus = Field(default=JobStatus.IDLE)
    json_content: str

    retries: int = 0
    max_retries: int = 3

    job_started_at: datetime

