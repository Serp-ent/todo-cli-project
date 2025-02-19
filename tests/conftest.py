import pytest
from todocli.models import TaskManager, Task
import json


@pytest.fixture(params=[0, 1, 5, 9])
def dir_with_n_tasks_file(tmpdir, request):
    """This directory contains file with n tasks"""
    n = request.param
    file = tmpdir / TaskManager.CONFIG_FILE
    data = {"tasks": [x for x in range(n)]}
    with open(file, "w") as f:
        json.dump(data, f)

    return tmpdir, n
