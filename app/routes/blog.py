import flask
from flask_login import login_required

from app.models.blog import Article
from app.utils.auth import admin_required
from app.forms.blog import NewBlogPostForm

blueprint = flask.Blueprint("blog", __name__)

@blueprint.route("/")
def index():
    return flask.render_template("blog/index.html")

@blueprint.route("/<slug>")
def article(slug):
    a = Article.query.filter_by(slug=slug).first()
    return str(a)

@blueprint.route("/new", methods=["GET", "POST"])
@admin_required
def new():
    form = NewBlogPostForm()

    if form.validate_on_submit():
        print(form.content.data)
        # TODO: Implement post

    return flask.render_template(
        'blog/new.html',
        form=form
    )