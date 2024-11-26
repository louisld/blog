import flask

main_blueprint = flask.Blueprint("main", __name__)

@main_blueprint.route("/")
def index():
    return flask.render_template("main/index.html")

@main_blueprint.route("/apropos")
def apropos():
    return flask.render_template("main/apropos.html")