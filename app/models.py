"""Database models used in the website."""

from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id: int) -> "User":
    """Returns the user given its id.

    Args:
        user_id (int): user id.

    Returns:
        User: user selected by user's id.
    """

    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """Represents a valid user.

    Args:
        id (int): id of the user.
        username (str): username of the user.
        email (str): email of the user.
        image_file (str): path of the user's icon.
        password (str): password of the user.
        posts (Post): posts written by the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def get_reset_token(self, expires_sec=1800) -> str:
        """Generates a password reset token for the user.

        Args:
            expires_sec (int, optional): Number of seconds in which the reset
                token is valid. Defaults to 1800.

        Returns:
            str: reset token generated for the user.
        """

        serial = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return serial.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        serial = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = serial.loads(token)["user_id"]
        # TODO: specify Exception
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        usertype = "Admin" if self.is_admin else "NormalUser"
        return f"{usertype}({self.username!r}, {self.email!r}, {self.image_file!r})"


class Post(db.Model):
    """Represents a post in the website.

    Args:
        id (int): id of the post.
        title (str): title of the post.
        date_posted (datetime.datetime): timestamp of the post creation.
        content (str): content of the post.
        user_id (id): id of the post owner.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post({self.title!r}, {self.date_posted!r})"
