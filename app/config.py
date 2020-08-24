import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.with_name(".env").absolute()
load_dotenv(dotenv_path)


class Config:
    MAIL_PASSWORD = os.environ.get("MAIL_PASS")
    MAIL_PORT = 587
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USER")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
