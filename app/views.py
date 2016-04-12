from app import app, mysql, login_manager
from flask import Flask, abort, request, jsonify, g, url_for, render_template, redirect, flash
from .forms import SignUpForm, LoginForm, IngredientForm
from .models import User
from flask.ext.login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    return render_template("home.html")


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
                user = User(email, password, firstname, lastname, year_of_birth)
                login_user(user)
                return redirect(url_for('add_ingredient'))
            except Exception as e:
                flash(str(e))
                return render_template('signup.html', form=form)
        else:
            flash('Error signing up')
            render_template('signup.html' , form=form)
    else:
        return render_template('signup.html', form=form)

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            try:
                cursor = mysql.cursor()
                cursor.execute('''select * from users where email="%s" and password="%s"''' % (email , password))
                result = cursor.fetchall()
                if not result:
                     flash('Invalid login credentials')
                     return render_template('login.html', form=form)
                else:
                    user = User(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])
                    login_user(user)
                    return 'LoggedIn'
            except Exception as e:
                return str(e)
        else:
           return render_template('login.html' , form=form)
    else:
        return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged Out'

@app.route('/add_ingredient')
@login_required
def add_ingredient():
    form = IngredientForm(csrf_enabled=False)
    cursor = mysql.cursor()
    cursor.execute('''select unit_name from units''')
    units = cursor.fetchall()
    choices = [(unit[0], unit[0].capitalize()) for unit in units]
    form.unit_name.choices = choices

    return render_template('add_ingredient.html', form=form)

@login_manager.user_loader
def load_user(email):
    try:
        cursor = mysql.cursor()
        cursor.execute('''select * from users where email="%s"''' % (email))
        result = cursor.fetchall()
        if not result:
            return None
        user = User(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])
        return user
    except Exception as e:
        print str(e)
        return None

