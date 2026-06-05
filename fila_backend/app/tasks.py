import time
from app.celery_app import celery_app
from app.database import SessionLocal
from app.models import Job


@celery_app.task(bind=True)
def process_job(self, job_id: int):
    db = SessionLocal()

    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            return "Job não encontrado"

        job.status = "processing"
        db.commit()

        time.sleep(10)

        job.status = "completed"
        job.result = f"Tarefa '{job.task_name}' processada com sucesso."
        db.commit()

        return job.result

    except Exception as e:
        job = db.query(Job).filter(Job.id == job_id).first()
        if job:
            job.status = "failed"
            job.result = str(e)
            db.commit()
        raise

    finally:
        db.close()