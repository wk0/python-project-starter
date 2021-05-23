from dotenv import load_dotenv

import logging
import datetime

from pathlib import Path


def config_env():
    load_dotenv()
    env_path = Path("../") / "../.env"
    load_dotenv(dotenv_path=env_path)

    # retrieving keys and adding them to the project
    # from the .env file through their key names
    #
    # SAMPLE_VAR = os.getenv("SAMPLE_VAR")


def config_logger(logname=None):
    if logname:
        filename = str(Path(f"../logs/{logname}.log"))
    else:
        filetime = str(datetime.datetime.now()).replace(" ", "_")
        filename = str(Path(f"../logs/{filetime}.log"))

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S",
        filename=filename,
        filemode="w",
    )
