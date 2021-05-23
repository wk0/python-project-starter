# conftest.py
# https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files

import pytest
from . import env_loader


@pytest.fixture()
def load_env():
    env_loader()
