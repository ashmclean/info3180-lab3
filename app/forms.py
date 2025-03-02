from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=64)])  # 1-64 characters
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=1, max=120)])  # 1-120 characters
    message = StringField('Message', validators=[DataRequired(), Length(min=1, max=8192)])  # 1-8192 characters 
    submit = SubmitField('Submit')