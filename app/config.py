from logging import basicConfig, getLogger
import os
from pathlib import Path
import sys

from dotenv import load_dotenv


def setup_dotenv():
    dotenv_path = Path(__file__).parent.with_name(".env").absolute()
    load_dotenv(dotenv_path)


def setup_logging():
    fmt = "[%(asctime)s] %(levelname)s - %(name)s:%(lineno)s - %(message)s"
    logging_path = Path(__file__).parent.with_name("axeh99.log").absolute()
    basicConfig(filename=logging_path, format=fmt, level=10)
    getLogger("werkzeug").setLevel(50)


setup_dotenv()
setup_logging()


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
    logger = getLogger(__name__)
    if not Config.SQLALCHEMY_DATABASE_URI:
        print("Error: SQLALCHEMY_DATABASE_URI not defined", file=sys.stderr)
        logger.critical("SQLALCHEMY_DATABASE_URI not defined")
        sys.exit(1)

    if not Config.SECRET_KEY:
        print("Error: SECRET_KEY not defined", file=sys.stderr)
        logger.critical("SECRET_KEY not defined")
        sys.exit(1)

    if not Config.MAIL_USERNAME:
        logger.warning("MAIL_USER not defined")

    if not Config.MAIL_PASSWORD:
        logger.warning("MAIL_PASS not defined")


check_config()
