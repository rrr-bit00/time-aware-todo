from datetime import datetime, func

from sqlmodel import DateTime, Field, SQLModel


class TodoBase(SQLModel):
    task_name: str = Field(max_length=60)
    is_completed: bool = Field(default=False)
    due_date: datetime | None


class TodoCreate(TodoBase):
    pass


class TodoBaseCompleted(TodoBase):
    completed_at: datetime | None


class TodoUpdate(SQLModel):
    task_name: str | None = Field(default=None, max_length=60)
    due_date: datetime | None = Field(default=None)
    is_completed: bool | None = Field(default=None)
    completed_at: datetime | None = Field(default=None)


class TodoCheck(TodoBase):
    is_completed: bool = True
    completed_at: datetime = Field(
        nullable=False,
        sa_type=DateTime(timezoe=True),
        sa_column_kwargs={"server_default": func.now()},
    )
