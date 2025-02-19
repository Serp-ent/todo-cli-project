import pytest
from todocli.models import TaskManager, Task
import json
import os


@pytest.fixture(params=[0, 1, 5, 9])
def dir_with_n_tasks_file(tmpdir, request):
    """This directory contains file with n tasks"""
    n = request.param
    file = tmpdir / TaskManager.CONFIG_FILE
    data = {"tasks": [x for x in range(n)]}
    with open(file, "w") as f:
        json.dump(data, f)

    return tmpdir, n


@pytest.fixture
def task_manager(tmp_path):
    # Mock HOME directory to temporary path
    os.environ["HOME"] = str(tmp_path)
    manager = TaskManager()
    yield manager
    # Cleanup after each test
    if manager.filepath.exists():
        manager.filepath.unlink()


