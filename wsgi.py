from pathlib import Path

activate_this_path = Path(__file__).parent.joinpath(".venv/bin/activate_this.py")
with activate_this_path.open() as file:
    exec(file.read(), dict(__file__=activate_this_path.as_posix()))

import sys

sys.path.insert(0, Path(__file__).parent.as_posix())
from app import create_app

application = create_app()
