import flask

from src.routes.main import bp

@bp.route("/")
def index():
    return flask.render_template("main/index.html")

@bp.route("/apropos")
def apropos():
    return flask.render_template("main/apropos.html")