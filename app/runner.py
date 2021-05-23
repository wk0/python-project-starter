import logging
import sys
import os

sys.path.append("../")

from app.config_loader import config_env, config_logger
from app.sample.sample import Sample

config_env()
config_logger()


def run_sample():
    sample_var = os.getenv("SAMPLE_VAR")
    logging.info(sample_var)

    sample = Sample(sample_var=sample_var)

    logging.info(sample.sample_var)

    sample.sample_func(sample_item="a")
    sample.sample_func(sample_item="b")
    sample.sample_func(sample_item="c")

    logging.info(sample.sample_list)


if __name__ == "__main__":
    run_sample()
