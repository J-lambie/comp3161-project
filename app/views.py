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

@app.route('/add_ingredient', methods=['GET' , 'POST'])
@login_required
def add_ingredient():
    form = IngredientForm(csrf_enabled=False)
    cursor = mysql.cursor()
    cursor.execute('''select unit_name from units''')
    units = cursor.fetchall()
    choices = [(unit[0], unit[0].capitalize()) for unit in units]
    form.unit_name.choices = choices
    if request.method == 'POST':
        if form.validate_on_submit():
            product_name = form.product_name.data
            calories_per_unit = form.calories_per_unit.data
            stock = form.stock.data
            cost = form.cost.data
            unit_name = form.unit_name.data
            email = current_user.email
            try:
                cursor.execute('''insert into ingredients (product_name, unit_name, email, calories_per_unit, stock, cost) values ("%s", "%s", "%s", %d, %d, %0.2f)''' % (product_name, unit_name, email, calories_per_unit, stock, cost))
                mysql.commit()
                return 'Added'
            except Exception as e:
                flash(str(e))
                return render_template('add_ingredient.html', form=form)
        else:
            flash('Error adding ingredient')
            return render_template('add_ingredient.html', form=form)
    else:
        return render_template('add_ingredient.html', form=form)

@app.route('/kitchen')
@login_required
def kitchen():
    cursor = mysql.cursor()
    cursor.execute('''select product_name, calories_per_unit, stock from ingredients where email="%s"''' % (current_user.email))
    result = cursor.fetchall()
    ingredients = []
    if result:
        ingredients = [{'product_name': ingredient[0], 'calories': ingredient[1], 'stock': ingredient[2]} for ingredient in result]
    return render_template('kitchen.html', ingredients=ingredients)

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

