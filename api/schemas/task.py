from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str | None = Field(None, example="슈퍼마켓에서 장 보기")

class TaskCreate(TaskBase): # TaskBase를 변경하지 않으면 동작 확인 시 title이 표시되지 않음
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="완료 플래그")

class Config:
    orm_mode = True