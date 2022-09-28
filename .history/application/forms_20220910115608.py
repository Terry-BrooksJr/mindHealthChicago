from flask_wtf import FlaskForm
from  wtforms import StringField, SubmitField, DateField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email
from .util import valid_phone


class ClientIntrestForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired('Please Enter First Name')])
    last_name = StringField("Last Name", validators=[DataRequired('Please Enter Last Name')])
    nickname = StringField("Preferred Name/Nickname")
    date = DateField("Preferred First Appointment Date", validators=[DataRequired('Please Select a Desired Date')])
    comment = TextAreaField('Anything You Want To Share With MindHealth Before Your Visit?')
    phone_number = StringField('Please Enter Contact Phone Number?', validators=[DataRequired('Please Enter Contact Number'), valid_phone])
    email= EmailField('Contact Email', validators=[DataRequired('Please Enter Email'), Email('Email is Invaild, Please Check Entry')])
    submit = SubmitField('Submit')
    