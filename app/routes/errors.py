import flask

from werkzeug.exceptions import HTTPException

blueprint = flask.Blueprint("errors", __name__)

@blueprint.app_errorhandler(404)
def not_found_error(error: HTTPException):
    message = error.description if hasattr(error, 'description') else 'Oops ! Cette page n\'existe pas !'

    return flask.render_template(
        "errors/404.html",
        message=message
    ), 404