import os
import sys
from warnings import warn

from dotenv import load_dotenv

load_dotenv()


class Config:
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
    MAIL_PORT = 587
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
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
