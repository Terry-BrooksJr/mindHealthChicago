from flask_wtf import FlaskForm
from  wtforms import StringField, SubmitField, DateField, TextAreaField, EmailField,IntegerField, ValidationError
from wtforms.validators import DataRequired, Email
import re
import string

#Custom Vaildator For Phone
def valid_phone():
        number = field.data
        number = number.translate(str.maketrans("", "", string.punctuation))
        pattern = r"1?\d{3}\d{3}\d{4}"
        number = number.strip()
        if number[0] == "1":
            test_number = number[1:]
            search = re.search(pattern, test_number)
        else:
            search = re.search(pattern, number)
        if search == None:
            raise ValidationError('Invaild Phone Number')
        else: 
            if len(search.group()) == 10:
                return True
            else:
                raise ValidationError('Invaild Phone Number')


class ClientIntrestForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired('Please Enter First Name')])
    last_name = StringField("Last Name", validators=[DataRequired('Please Enter Last Name')])
    nickname = StringField("Preferred Name/Nickname")
    date = DateField("Preferred First Appointment Date", validators=[DataRequired('Please Select a Desired Date')])
    comment = TextAreaField('Anything You Want To Share With MindHealth Before Your Visit?')
    phone_number = StringField('Please Enter Contact Phone Number?', validators=[
                                DataRequired('Please Enter Contact Number'), valid_phone])
    email= EmailField('Contact Email', validators=[DataRequired('Please Enter Email'), Email('Email is Invaild, Please Check Entry')])
    submit = SubmitField('Submit')

    