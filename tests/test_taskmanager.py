from todocli.models import TaskManager, Task
from datetime import datetime


def test_task_create_file_is_not_found(tmpdir, monkeypatch):
    # Arrange
    monkeypatch.setenv("HOME", str(tmpdir))

    # Act
    manager = TaskManager()

    # Assert
    assert manager.get_filepath() == (tmpdir / TaskManager.CONFIG_FILE)
    assert len(manager.tasks) == 0


def test_task_opening_tasks_file_with_records(monkeypatch, dir_with_n_tasks_file):
    ntasksdir, want = dir_with_n_tasks_file
    # Arrange
    monkeypatch.setenv("HOME", str(ntasksdir))

    # Act
    manager = TaskManager()

    # Assert
    assert manager.get_filepath() == (ntasksdir / TaskManager.CONFIG_FILE)
    assert len(manager.tasks) == want
