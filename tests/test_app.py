from .context import runner

import logging
import os


def test_runner(caplog):
    # init test logger
    caplog.set_level(logging.INFO)

    # run testable code
    runner.run_sample()

    # ensure messages add up
    log_messages = [rec.message for rec in caplog.records]

    assert len(log_messages) == 3
    assert log_messages[0] == os.getenv("SAMPLE_VAR")
    assert log_messages[1] == os.getenv("SAMPLE_VAR")
    assert log_messages[2] == str(["a", "b", "c"])
