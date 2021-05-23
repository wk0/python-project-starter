# test_config.py
import os
import logging

from .context import app


def test_base():
    assert True


def test_env():
    assert os.getenv("SAMPLE_VAR") == "filler"


def test_log(caplog):
    # https://docs.pytest.org/en/stable/logging.html
    caplog.set_level(logging.INFO)
    logmsg = "test write to log"

    logging.info(logmsg)

    log_messages = [rec.message for rec in caplog.records]

    assert len(log_messages) == 1
    assert log_messages[0] == logmsg
