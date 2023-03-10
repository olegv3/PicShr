from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Image

class ImageForm(FlaskForm):
    title = StringField('Title')
    description = StringField('Description')
    tags = StringField('Tags')
    people = StringField('People')
    albums = IntegerField('Album')
