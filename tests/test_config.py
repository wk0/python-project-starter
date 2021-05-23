# test_config.py
import os

from .context import app


def test_base():
    assert True


def test_env():
    assert os.getenv("SAMPLE_VAR") == "filler"
