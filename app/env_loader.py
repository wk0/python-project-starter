from dotenv import load_dotenv

from pathlib import Path


def load_env():
    load_dotenv()
    env_path = Path("../") / "../.env"
    load_dotenv(dotenv_path=env_path)

    # retrieving keys and adding them to the project
    # from the .env file through their key names
    #
    # SAMPLE_VAR = os.getenv("SAMPLE_VAR")
