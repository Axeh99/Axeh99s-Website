from logging import basicConfig
import os
from pathlib import Path
import sys
from warnings import warn

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.with_name(".env").absolute()
basicConfig(filename=dotenv_path.with_name("axeh99.log"))
load_dotenv(dotenv_path)


class Config:
    ROOT_PATH = Path(__file__).parent.parent.absolute()
    MAIL_PASSWORD = os.environ.get("MAIL_PASS")
    MAIL_PORT = 587
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USER")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + ROOT_PATH.joinpath("data.sqlite").as_posix()
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def check_config():
    if not Config.SQLALCHEMY_DATABASE_URI:
        print("Error: SQLALCHEMY_DATABASE_URI not defined", file=sys.stderr)
        sys.exit(1)

    if not Config.SECRET_KEY:
        print("Error: SECRET_KEY not defined", file=sys.stderr)
        sys.exit(1)

    if not Config.MAIL_USERNAME:
        warn("Warning: MAIL_USER not defined")

    if not Config.MAIL_PASSWORD:
        warn("Warning: MAIL_PASS not defined")


check_config()
