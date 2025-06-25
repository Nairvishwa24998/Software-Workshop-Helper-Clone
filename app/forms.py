from flask_wtf import FlaskForm

from wtforms import SubmitField, HiddenField, SelectField, IntegerField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Name of the Student', validators=[DataRequired()])
    seat_number = StringField('Seat Number', validators=[DataRequired()])
    topic = SelectField("Topic", choices=[("PyCharm/Conda/Flask issue","PyCharm/Conda/Flask issue"),("HTML/CSS/Bootstrap issue","HTML/CSS/Bootstrap issue"),("Code bug/error","Code bug/error"),("Understanding the lab exercises","Understanding the lab exercises"),("Other","Other")])
    submit = SubmitField("Submit")






