import flask

blog_blueprint = flask.Blueprint("blog", __name__)

@blog_blueprint.route("/")
def index():
    return flask.render_template("blog/index.html")