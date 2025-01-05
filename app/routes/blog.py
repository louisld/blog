from datetime import datetime

import flask
from flask import g, url_for

from app import db
from app.models.blog import Article
from app.utils.auth import admin_required
from app.forms.blog import NewBlogPostForm, EditBlogPostForm

blueprint = flask.Blueprint("blog", __name__)

@blueprint.route("/")
def index():
    articles = Article.query.order_by(Article.updated_at.desc()).all()
    return flask.render_template(
        "blog/index.html",
        articles=articles
    )

@blueprint.route("/<slug>")
def article(slug):
    a = Article.query.filter_by(slug=slug).first()
    if a is None:
        return flask.abort(404, description="L'article demandé n'existe pas !")
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

@blueprint.route("/edit/<slug>", methods=["GET", "POST"])
@admin_required
def edit(slug):
    a = Article.query.filter_by(slug=slug).first()
    if a is None:
        flask.abort(404, description="L'article que vous voulez éditer n'existe pas !")
    form = EditBlogPostForm(obj=a)

    if form.validate_on_submit():
        a.title = form.title.data
        a.content = form.content.data
        a.updated_at = datetime.now()

        db.session.commit()

        return flask.redirect(url_for(
            "blog.article", slug=a.slug
        ))

    return flask.render_template(
        'blog/edit.html',
        form=form
    )