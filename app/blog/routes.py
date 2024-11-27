import flask

from app.blog.models import Article

blog_blueprint = flask.Blueprint("blog", __name__)

@blog_blueprint.route("/")
def index():
    return flask.render_template("blog/index.html")

@blog_blueprint.route("/<slug>")
def article(slug):
    a = Article.query.filter_by(slug=slug).first()
    return str(a)