from flask_wtf import FlaskForm

from wtforms.widgets import TextArea, html_params
from wtforms.fields import TextAreaField
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import (
    DataRequired
)

from markupsafe import (
    escape,
    Markup
)

class MarkdownWidget(TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault("style", "display: none;")
        html = super().__call__(field, **kwargs)
        return html + Markup(
            f"<div id='cm-editor-{field.id}'></div>"
        )
        
    

class MarkdownField(TextAreaField):

    widget = MarkdownWidget()

class NewBlogPostForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    content = MarkdownField('Contenu')
    submit = SubmitField('Créer un nouveau post')