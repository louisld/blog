from functools import wraps

from flask import g

def admin_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        print(g.logged_in)
        return False
    return decorated_func