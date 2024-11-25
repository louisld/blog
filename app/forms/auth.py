from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Length
)

class LoginForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[
        DataRequired(),
        Length(min=8)
    ])
    remember_me = BooleanField("Se souvenir de moi")
    submit = SubmitField('Se connecter')