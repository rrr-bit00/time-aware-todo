import uuid

from datetime import datetime, func
from sqlmodel import Field, DateTime, Relationship

from schemas.users import UserBase
from models.tasks import Task
from models.todos import Todo
from models.screen_times import Screen_time

# Base = declarative_base()


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hash_password: str
    # 3つの子テーブルに対してリレーション
    tasks: list["Task"] = Relationship(back_populates="user", cascade_delete=True)
    todos: list["todo"] = Relationship(back_populates="user", cascade_delete=True)
    screen_times: list["Screen_time"] = Relationship(
        back_populates="user", cascade_delete=True
    )

    create_at: datetime = Field(
        nullable=False,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"onupdate": func.now(), "sever_default": func.now()},
    )
    update_at: datetime = Field(
        nullable=False,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"onupdate": func.now(), "sever_default": func.now()},
    )
