![Batch-Process](/assets/batch-process.png)

## start celery worker

`
celery -A config.celery.celery worker --concurrency=3 --loglevel=info
`

## start publishing jobs

`
python -m tests.test_celery
`