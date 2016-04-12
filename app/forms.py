from flask.ext.wtf import Form
from wtforms import TextField, SelectField, PasswordField,FieldList,FormField

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
    
class InstructionForm(Form):
    instruction1=TextField('instruction1')
    instruction2=TextField('instruction2')
    instruction3=TextField('instruction3')
    instruction4=TextField('instruction4')
    
class RecipeForm(Form):
    recipe_name=TextField('recipe_name')
    image_url=TextField('image_url')
    calories=TextField('calories')
    instructions=FieldList(FormField(InstructionForm))