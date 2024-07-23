import flask

bp = flask.Blueprint("blog", __name__)

from src.routes.blog import routes