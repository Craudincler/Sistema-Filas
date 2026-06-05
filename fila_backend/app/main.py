from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Job
from app.schemas import JobCreate, JobResponse
from app.tasks import process_job

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Filas com FastAPI + Celery")


@app.get("/")
def home():
    return {"message": "API no ar"}


@app.post("/jobs", response_model=JobResponse)
def create_job(payload: JobCreate, db: Session = Depends(get_db)):
    job = Job(task_name=payload.task_name, status="pending")
    db.add(job)
    db.commit()
    db.refresh(job)

    process_job.delay(job.id)

    return job


@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job não encontrado")

    return job