import flask

blueprint = flask.Blueprint("main", __name__)

@blueprint.route("/")
def index():
    return flask.render_template("main/index.html")

@blueprint.route("/apropos")
def apropos():
    return flask.render_template("main/apropos.html")