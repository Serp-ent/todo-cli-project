from datetime import datetime
from enum import Enum
from todocli import validators
from pathlib import Path
import json
import os


class Task:
    class Status(Enum):
        ACTIVE = "active"
        COMPLETED = "completed"

        @classmethod
        def from_str(cls, value: str):
            """Converts string to corresponding enum value"""
            try:
                return cls[value.upper().removeprefix('STATUS.')]
            except KeyError:
                raise ValueError(f"Invalid status value: {value}")

    def __init__(
        self,
        title: str,
        description: str,
        due_date: str | datetime,
        created_at: str | datetime = datetime.now(),
        status=Status.ACTIVE,
    ):
        if isinstance(due_date, str):
            due_date = datetime.fromisoformat(due_date)
        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at)
        if isinstance(status, str):
            status = Task.Status.from_str(status)

        self.title = validators.validate_title(title)
        self.description = description
        self.due_date = validators.validate_future_date(due_date)

        self.created_at = created_at
        self.status = status

    def __str__(self) -> str:
        return self.title

    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": str(self.due_date),
            "status": str(self.status),
            "created_at": str(self.created_at),
        }


class TaskManager:
    CONFIG_FILE = "task-cli.json"

    def __init__(self):
        self.filepath = Path(os.getenv("HOME")) / TaskManager.CONFIG_FILE

        if not os.path.exists(self.filepath):
            self.tasks = []
            return

        with open(self.filepath, "r") as f:
            data = json.load(f)
            self.tasks = [Task(**task) for task in data.get("tasks", [])]

    def save(self) -> None:
        """Save tasks to the JSON file"""
        tasks_json = [task.to_json() for task in self.tasks]

        with open(self.filepath, "w") as f:
            json.dump(
                {
                    "tasks": tasks_json,
                },
                f,
            )

    def get_filepath(self) -> str:
        return self.filepath

    def create(self, title, description, due_date) -> Task:
        task = Task(title, description, due_date)
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks

    def retrieve_task(self, n) -> Task:
        """Returns n-th saved task"""
        if n < 0:
            raise IndexError("Cannot retrieve Task (Index Out of Bounds)")
        return self.tasks[n]

    def update(self, n, title=None, description=None, due_date=None) -> Task:
        """Update the task at index n with new values for title, description, or due_date"""
        if n < 0 or len(self.tasks) <= n:
            raise IndexError("Cannot update Task (Index Out of Bounds)")

        task = self.tasks[n]

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if due_date is not None:
            task.due_date = due_date

        return task

    def delete(self, n) -> Task:
        if n < 0 or len(self.tasks) <= n:
            raise IndexError("Cannot delete Task (Index Out of Bounds)")
        return self.tasks.pop(n)
