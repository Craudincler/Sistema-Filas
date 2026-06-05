from sqlalchemy import Column, Integer, String
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, nullable=False)
    status = Column(String, default="pending")
    result = Column(String, nullable=True)