import flask

bp = flask.Blueprint("main", __name__)

from src.routes.main import routes