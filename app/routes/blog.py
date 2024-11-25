import flask

bp = flask.Blueprint("blog", __name__)

@bp.route("/")
def index():
    return flask.render_template("blog/index.html")