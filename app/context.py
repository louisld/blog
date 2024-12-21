import typing

from flask import g
from flask_login import current_user, AnonymousUserMixin

from app.models.auth import User

def create_request_context():
    g.logged_in = False
    g.logged_in_user = None
    g.user = None

    cu = typing.cast(AnonymousUserMixin | User, current_user)
    g.logged_in = cu.is_authenticated
    if g.logged_in:
        g.logged_in_user = typing.cast(User, current_user)
        g.user = g.logged_in_user

    return None
