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

    def __init__(self, title: str, description: str, due_date: datetime):
        self.title = validators.validate_title(title)
        self.description = description
        self.due_date = validators.validate_future_date(due_date)

        self.created_at = datetime.now()
        self.status = Task.Status.ACTIVE

    def __str__(self) -> str:
        return self.title


class TaskManager:
    CONFIG_FILE = "task-cli.json"

    def __init__(self):
        self.filepath = Path(os.getenv("HOME")) / TaskManager.CONFIG_FILE

        if not os.path.exists(self.filepath):
            self.tasks = []
            return

        with open(self.filepath, "r") as f:
            data = json.load(f)
            self.tasks = data.get("tasks")

    def save(self) -> None:
        """Save tasks to the JSON file"""
        with open(self.filepath, "w") as f:
            json.dump({"tasks": self.tasks}, f)

    def get_filepath(self) -> str:
        return self.filepath

    # TODO: create
    # TODO: read
    # TODO: update
    # TODO: delete
