import pytest
from todocli.models import Task
from datetime import datetime, timedelta


@pytest.mark.parametrize(
    "title,description",
    [
        ("title1", "desc1"),
        ("title2", "desc2"),
        ("title3", "desc3"),
    ],
)
def test_valid_task_creation(title, description):
    # Arrange
    next_day = datetime.now() + timedelta(days=1)
    # Act
    task = Task(title=title, description=description, due_date=next_day)
    # Assert
    assert task.title == title
    assert task.description == description
    assert task.status == Task.Status.ACTIVE, "Task should be active by default"


@pytest.mark.parametrize(
    "delta",
    [
        {"hours": 1},
        {"days": 1},
    ],
    ids=[
        "1 hour in the future",
        "1 day in the future",
    ],
)
def test_task_due_date_in_the_future(delta):
    """This test checks if valid due_date doesn't throw validation errors"""
    # Arrange
    today = datetime.today()
    prev_day = today + timedelta(**delta)
    # Act
    task = Task("name", "desc", prev_day)

    assert task.due_date == prev_day


@pytest.mark.parametrize(
    "delta",
    [
        {"hours": 1},
        {"days": 1},
    ],
    ids=[
        "1 hour in the past",
        "1 day in the past",
    ],
)
def test_task_due_date_in_the_past(delta):
    today = datetime.today()
    prev_day = today - timedelta(**delta)

    with pytest.raises(ValueError, match="Due date cannot be in the past"):
        Task(title="title", description="desc", due_date=prev_day)


@pytest.mark.parametrize(
    "title", [None, ""], ids=["Title is None", "Title is empty string"]
)
def test_task_title_cannot_be_empty(title):
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(
            title=title,
            description="",
            due_date=datetime.now() + timedelta(days=1),
        )


@pytest.mark.parametrize("task_name", ["name1", "name2"])
def test_str_representation(task_name):
    task = Task(task_name, "desc", due_date=datetime.now() + timedelta(days=1))

    assert str(task) == task.title
    assert str(task) == task_name
