import datetime

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

def format_date_full(dt: datetime):
    return f"{dt.day} {MONTHS[dt.month - 1]} {dt.year}"