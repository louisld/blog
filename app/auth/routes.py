import flask
from flask import redirect, url_for, current_app, session, request
from flask_login import current_user, login_user, logout_user

from app.auth.models import User
from app.auth.forms import LoginForm

auth_blueprint = flask.Blueprint("auth", __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    print("--------------------------------")
    print(request.headers)
    print(request.form)
    print(dict(session))
    form = LoginForm()
    print(form.csrf_token.current_token)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flask.flash('Identifiants incorrects.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    print(form.errors)
    return flask.render_template(
        "auth/login.html",
        form=form
    )

@auth_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))