import flask

from app.models.blog import Article
from app.utils.auth import admin_required

blueprint = flask.Blueprint("blog", __name__)

@blueprint.route("/")
def index():
    return flask.render_template("blog/index.html")

@blueprint.route("/<slug>")
def article(slug):
    a = Article.query.filter_by(slug=slug).first()
    return str(a)

@blueprint.route("/new")
@admin_required
def new():
    return "Salut"