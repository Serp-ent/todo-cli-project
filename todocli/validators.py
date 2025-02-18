from datetime import datetime

def validate_future_date(time: datetime) -> datetime:
    if time < datetime.now():
        raise ValueError("Due date cannot be in the past")

    return time


def validate_title(title: str) -> str:
    if title is None or title == "":
        raise ValueError("Title cannot be empty")

    return title.strip()