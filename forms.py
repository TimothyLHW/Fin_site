from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  # Add this line
    submit = SubmitField('Login')

class IncomeForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    submit = SubmitField('Add Income')

class ExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Expense')

