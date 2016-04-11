from flask.ext.wtf import Form
from wtforms import TextField, SelectField, PasswordField

class SignUpForm(Form):
    email = TextField('email')
    firstname = TextField('firstname')
    lastname = TextField('lastname')
    password = PasswordField('password')
    year_of_birth = SelectField('year_of_birth')

    choices = [(str(x),x) for x in range(1900,2003)]
    year_of_birth.choices = choices
    
