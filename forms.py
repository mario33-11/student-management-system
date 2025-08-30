from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from datetime import date

class StudentForm(FlaskForm):
    """Form for creating and editing student information"""
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=20)])
    department = StringField('Department', validators=[DataRequired(), Length(min=2, max=50)])
    enrollment_date = DateField('Enrollment Date', validators=[DataRequired()], default=date.today)
    submit = SubmitField('Save Student')

class SearchForm(FlaskForm):
    """Form for searching students by ID, Name or Email"""
    search_query = StringField('Search by ID, Name or Email', validators=[DataRequired()])
    submit = SubmitField('Search')
