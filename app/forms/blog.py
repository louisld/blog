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

from app.forms.validators import (
    Slug
)

class MarkdownWidget(TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault("style", "display: none;")
        html = super().__call__(field, **kwargs)

        return Markup(
            f"<div id='cm-editor-{field.id}'></div>"
        ) + html


class NewBlogPostForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired(), Slug()])
    content = TextAreaField('Contenu', widget=MarkdownWidget())
    submit = SubmitField('Créer un nouveau post')

class EditBlogPostForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    slug = StringField(
        'Slug',
        validators=[DataRequired(), Slug()],
        render_kw={"readonly": True}
    )
    content = TextAreaField('Contenu', widget=MarkdownWidget())
    submit = SubmitField('Mettre à jour le post')