# conftest.py
# https://stackoverflow.com/questions/34466027/in-pytest-what-is-the-use-of-conftest-py-files

import pytest
from . import config_loader


@pytest.fixture()
def load_env():
    config_loader.config_env()


@pytest.fixture()
def load_logger():
    config_loader.config_logger("test")
