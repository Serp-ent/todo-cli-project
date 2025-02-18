from datetime import datetime
from enum import Enum
from todocli import validators


class Task:
    class Status(Enum):
        ACTIVE = "active"
        COMPLETED = "completed"

    def __init__(self, title: str, description: str, due_date: datetime):
        self.title = validators.validate_title(title)
        self.description = description
        self.due_date = validators.validate_future_date(due_date)

        self.created_at = datetime.now()
        self.status = Task.Status.ACTIVE

    def __str__(self) -> str:
        return self.title


class TaskManager():
    # TODO: create
    # TODO: read
    # TODO: update
    # TODO: delete

    # TODO: save to .json file
    # TODO: load task from JSON on startup