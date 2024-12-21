import flask
from flask import redirect, url_for, current_app, session, request
from flask_login import current_user, login_user, logout_user, login_required

from app.models.auth import User
from app.forms.auth import LoginForm

blueprint = flask.Blueprint("auth", __name__)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flask.flash('Identifiants incorrects.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return flask.render_template(
        "auth/login.html",
        form=form
    )

@blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))