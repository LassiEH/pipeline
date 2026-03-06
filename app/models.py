from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func
from .db import Base

class URLResult(Base):
    __tablename__ = "url_results"

    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    status_code = Column(Integer)
    response_ms = Column(Integer)
    error_msg = Column(Text, nullable=True)
    processed_at = Column(TIMESTAMP, server_default=func.now())