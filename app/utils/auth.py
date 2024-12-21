from functools import wraps

from flask import g, redirect, url_for, request

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(g.user)
        if g.user is not None and g.user.is_admin:
            return f(*args, **kwargs)
        return redirect(url_for('auth.login'))
    return decorated_function