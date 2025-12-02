import uuid
from datetime import datetime, func

from sqlmodel import DateTime, Field

from schemas.todos import TodoBase


class Todos(TodoBase):
    id: int = Field(default_factory=uuid.uuid4, primary_key=True)

    completed_at: datetime = Field(
        nullable=False,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now()},
    )
    created_at: datetime = Field(
        nullable=False,
        sa_type=datetime(timezone=True),
        sa_columns_kwargs={"server_default": func.now()},
    )
