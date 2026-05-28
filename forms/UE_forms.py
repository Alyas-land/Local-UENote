from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length



class AddProject(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(min=3, message='The title must be equal or bigger than 3 character!')])
    description = TextAreaField(validators=[InputRequired(), Length(min=3, message='The description must be equal or bigger than 3 character!')])
    create = SubmitField("Create")