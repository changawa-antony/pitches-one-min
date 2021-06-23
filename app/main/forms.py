from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content',validators=[Required()])
    submit = SubmitField('submit')

