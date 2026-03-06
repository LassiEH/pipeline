from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

from sqlalchemy.orm import Session

from .tasks import fetch_url
from .db import SessionLocal, Base, engine
from .models import URLResult

Base.metadata.create_all(bind=engine)
app = FastAPI()


class AnalyzeRequest(BaseModel):
    urls: List[str]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/analyze")
def analyze(data: AnalyzeRequest):
    if len(data.urls) > 10:
        raise HTTPException(status_code=400, detail="Max 10 URLs per request")

    for url in data.urls:
        fetch_url.delay(url)

    return {"queued": len(data.urls)}


@app.get("/results")
def get_results(db: Session = Depends(get_db)):
    results = db.query(URLResult).all()

    return [
        {
            "url": r.url,
            "status_code": r.status_code,
            "response_ms": r.response_ms,
            "error_msg": r.error_msg,
            "processed_at": r.processed_at,
        }
        for r in results
    ]