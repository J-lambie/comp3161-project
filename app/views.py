from app import app, mysql
from flask import Flask, abort, request, jsonify, g, url_for, render_template, redirect
from .forms import SignUpForm

@app.route('/')
def home():
    return "I'm home"

@app.route('/signup' ,methods=['GET' , 'POST'])
def signup():
    form = SignUpForm(csrf_enabled=False)
    choices = [(str(x),x) for x in reversed(range(1900,2004))]
    form.year_of_birth.choices = choices
    if request.method == 'POST': 
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            firstname = form.firstname.data
            lastname = form.lastname.data
            year_of_birth = form.year_of_birth.data
            try:
                cur = mysql.cursor()
                cur.execute('''insert into users values ('%s', '%s', '%s','%s', %d)''' % (email , password,firstname, lastname, int(year_of_birth)))
                mysql.commit()
                return email
            except Exception as e:
                return str(e)
        else:
            render_template('signup.html' , form=form)
    else:
        return render_template('signup.html', form=form)
