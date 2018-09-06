from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class GifForm (FlaskForm):
    searchterm = StringField(validators=[DataRequired()])
