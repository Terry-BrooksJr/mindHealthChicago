from wtforms import ValidationError
import re
import string


#Custom Vaildator For Phone
def valid_phone(field):
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
