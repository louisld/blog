from datetime import datetime

import flask
from flask import g, url_for

from app import db
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
    return flask.render_template(
        'blog/article.html',
        article=a
    )

@blueprint.route("/new", methods=["GET", "POST"])
@admin_required
def new():
    form = NewBlogPostForm()

    if form.validate_on_submit():
        a = Article()
        form.populate_obj(a)
        a.created_at = datetime.now()
        a.updated_at = a.created_at
        a.author = g.user

        db.session.add(a)
        db.session.commit()

        return flask.redirect(url_for(
            "blog.article", slug=a.slug
        ))


    return flask.render_template(
        'blog/new.html',
        form=form
    )