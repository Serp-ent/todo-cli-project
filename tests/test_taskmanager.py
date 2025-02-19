import pytest
from todocli.models import TaskManager, Task
import os
import json
from datetime import datetime, timedelta


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


def test_initialization_with_no_existing_file(task_manager):
    assert len(task_manager.get_tasks()) == 0
    assert task_manager.filepath.exists() is False


def test_create_and_save_task(task_manager):
    test_task = task_manager.create(
        title="Test Task",
        description="Test Description",
        due_date=datetime.now() + timedelta(days=1),
    )

    # Test in-memory storage
    assert len(task_manager.get_tasks()) == 1
    assert task_manager.retrieve_task(0).title == "Test Task"

    # Test file persistence
    task_manager.save()
    assert task_manager.filepath.exists()

    with open(task_manager.filepath) as f:
        data = json.load(f)
        assert len(data["tasks"]) == 1
        assert data["tasks"][0]["title"] == "Test Task"


def test_load_existing_tasks(tmp_path):
    # Create test data
    test_data = {
        "tasks": [
            {
                "title": "Loaded Task",
                "description": "Loaded Description",
                "due_date": (datetime.now() + timedelta(days=2)).isoformat(),
                "created_at": datetime.now().isoformat(),
                "status": "active",
            }
        ]
    }

    test_file = tmp_path / "task-cli.json"
    with open(test_file, "w") as f:
        json.dump(test_data, f)

    # Test loading
    os.environ["HOME"] = str(tmp_path)
    manager = TaskManager()

    assert len(manager.get_tasks()) == 1
    task = manager.retrieve_task(0)
    assert task.title == "Loaded Task"
    assert task.status == Task.Status.ACTIVE


def test_delete_task(task_manager):
    # Add multiple tasks
    task_manager.create("First", "Desc1", datetime.now() + timedelta(days=1))
    task_manager.create("Second", "Desc2", datetime.now() + timedelta(days=2))
    task_manager.save()

    # Delete first task
    deleted = task_manager.delete(0)
    assert deleted.title == "First"
    assert len(task_manager.get_tasks()) == 1

    # Verify file update after save
    task_manager.save()
    with open(task_manager.filepath) as f:
        data = json.load(f)
        assert len(data["tasks"]) == 1
        assert data["tasks"][0]["title"] == "Second"


def test_retrieve_task_boundary_conditions(task_manager):
    task_manager.create("Test", "Desc", datetime.now() + timedelta(days=1))

    # Test valid index
    assert task_manager.retrieve_task(0).title == "Test"

    # Test invalid index
    with pytest.raises(IndexError):
        task_manager.retrieve_task(1)

    # Test negative index
    with pytest.raises(IndexError):
        task_manager.retrieve_task(-1)


def test_delete_empty_manager(task_manager):
    with pytest.raises(IndexError):
        task_manager.delete(0)
