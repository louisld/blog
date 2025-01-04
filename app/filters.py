import datetime

import mistletoe
import flask
from markupsafe import Markup

MONTHS = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre"
]

def register_filters(app: flask.Flask):
    def register(name, fun):
        app.jinja_env.filters[name] = fun
    register("format_date_full", format_date_full)
    register("markdown", markdown)

def format_date_full(dt: datetime):
    return f"{dt.day} {MONTHS[dt.month - 1]} {dt.year}"

def markdown(text: str):
    return Markup(mistletoe.markdown(text))