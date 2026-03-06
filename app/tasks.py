import time
import requests
from .celery_app import celery
from .db import SessionLocal
from .models import URLResult

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=5, max_retries=3)
def fetch_url(self, url: str):
    db = SessionLocal()

    start = time.time()

    error_msg = None
    try:
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
        except requests.RequestException as e:
            status = None
            error_msg = str(e)

        duration = int((time.time() - start) * 1000)

        result = URLResult(
            url=url,
            status_code=status,
            response_ms=duration,
            error_msg=error_msg,
        )

        db.add(result)
        db.commit()

    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()