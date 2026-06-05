from pydantic import BaseModel


class JobCreate(BaseModel):
    task_name: str


class JobResponse(BaseModel):
    id: int
    task_name: str
    status: str
    result: str | None = None

    class Config:
        from_attributes = True