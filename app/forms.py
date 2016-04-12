from flask.ext.wtf import Form
from wtforms import TextField, SelectField, PasswordField, IntegerField, FloatField

class SignUpForm(Form):
    email = TextField('email')
    firstname = TextField('firstname')
    lastname = TextField('lastname')
    password = PasswordField('password')
    year_of_birth = SelectField('year_of_birth')

    choices = [(str(x),x) for x in range(1900,2003)]
    year_of_birth.choices = choices

class LoginForm(Form):
    email = TextField('email')
    password = PasswordField('password')

class IngredientForm(Form):
    product_name = TextField('product_name')
    unit_name = SelectField('unit_name')
    calories_per_unit =  IntegerField('calories_per_unit')
    cost = FloatField('cost')
    stock = IntegerField('stock')

    
