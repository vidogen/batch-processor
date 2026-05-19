![Batch-Process](/assets/batch-process.png)

## batch processor

The batch processor is designed as a reusable layer for multiple Gen AI pipelines.

#### reusable flows:
- character sheet image generation
- character json generation
- episode json generation
- scene json generation
- bg audio generation
- dialog audio generation

![Pipelines](/assets/pipelines.png)

#### architecture notes:
- Redis is used as the message broker / queue
- Celery workers process jobs asynchronously
- workers support concurrent job execution using event loop based async processing
- jobs are independent and processed in parallel
- different pipelines can reuse the same batch processor with custom handlers/services

## start celery worker

```bash id="8b9n2c"
celery -A config.celery.celery worker --concurrency=3 --loglevel=info
```

* `-A`
  → tells Celery where the Celery app instance exists

* `--concurrency=3`
  → this single worker can process 3 jobs in parallel

* running 4 workers with concurrency 3:
  → `4 × 3 = 12` parallel jobs

## start publishing jobs

```bash id="k3v7qp"
python -m tests.test_celery
```