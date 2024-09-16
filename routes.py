from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, IncomeForm, ExpenseForm
from app.models import User, Income, Expense
from flask_login import login_user, current_user, logout_user, login_required

# Route for registration
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:  # Redirect to home if already logged in
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# Route for login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Redirect to home if already logged in
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')  # Error message
    return render_template('login.html', title='Login', form=form)

# Route for logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Route for adding income
@app.route("/add_income", methods=['GET', 'POST'])
@login_required
def add_income():
    form = IncomeForm()
    if form.validate_on_submit():
        income = Income(amount=form.amount.data, source=form.source.data, user_id=current_user.id)
        db.session.add(income)
        db.session.commit()
        flash('Income has been added!', 'success')
        return redirect(url_for('home'))  # Redirect to a home or dashboard route you will create
    return render_template('add_income.html', title='Add Income', form=form)

# Route for adding expense
@app.route("/add_expense", methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        expense = Expense(amount=form.amount.data, category=form.category.data, description=form.description.data, user_id=current_user.id)
        db.session.add(expense)
        db.session.commit()
        flash('Expense has been added!', 'success')
        return redirect(url_for('home'))  # Redirect to a home or dashboard route you will create
    return render_template('add_expense.html', title='Add Expense', form=form)

# Home route (placeholder)
@app.route("/home")
@login_required
def home():
    return render_template('home.html', title='Home')
