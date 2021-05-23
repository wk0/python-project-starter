import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app

app.config_loader.config_env()
app.config_loader.config_logger()
