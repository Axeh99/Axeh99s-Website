"""HTTP error handlers."""

import logging

from flask import Blueprint, render_template
from werkzeug.exceptions import Forbidden, InternalServerError, NotFound

errors = Blueprint("errors", __name__)
logger = logging.getLogger(__name__)


@errors.app_errorhandler(404)
def error_404(error: NotFound):  # pylint: disable=unused-argument
    logger.critical(error)
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(403)
def error_403(error: Forbidden):  # pylint: disable=unused-argument
    logger.critical(error)
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500)
def error_500(error: InternalServerError):  # pylint: disable=unused-argument
    logger.critical(error)
    return render_template("errors/500.html"), 500
