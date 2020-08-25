"""Common operations related to users."""

import logging
from pathlib import Path
import secrets

from PIL import Image
from flask import current_app, url_for
from flask_mail import Message

from app import mail

logger = logging.getLogger(__name__)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    picture_name = random_hex + Path(form_picture.filename).suffix
    pictures_folder = Path(current_app.root_path).joinpath("static/profile_pics")
    pictures_folder.mkdir(exist_ok=True, parents=True)
    picture_path = pictures_folder / picture_name

    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request",
        sender="elesmoquinado@gmail.com",
        recipients=[user.email],
    )
    message = (
        "To reset your password, visit the following link:\n"
        f"{url_for('users.reset_token', token=token, _external=True)}\n"
        "If you did not make this request then simply ignore this email "
        "and no changes will be made."
    )

    msg.body = message
    mail.send(msg)

    logger.debug("Sent reset email to %r", user.email)
