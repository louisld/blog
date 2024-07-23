import flask

from src.routes.blog import bp

@bp.route("/")
def index():
    return flask.render_template("blog/index.html")