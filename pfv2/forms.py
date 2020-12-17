from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import validators
from pfv2 import db
from pfv2.models import Account, AccountType, Budget

# class TestForm(FlaskForm):
#     account = StringField('Account', validators=[DataRequired()])
#     account_type = SelectField('Account Type', choices=[('savings', "Savings"), ('checking', 'Checking')])
#     submit = SubmitField('Create Account')

class AddAccountType(FlaskForm):
    account_type = StringField(label='Account Type', 
                                validators=[validators.required()], 
                                render_kw={"placeholder": "Checking", "class": "form-control"})
    submit = SubmitField(label='Add Account Type', render_kw={"class": "btn btn-primary"})



class AddAccount(FlaskForm):
    account_name = StringField(label="Account Name",validators=[validators.required()],
                                render_kw={"placeholder": "Checking", "class": "form-control"})
    account_type = SelectField(label="Account Type", render_kw={"class": "form-control"})
    initial_balance = StringField(label='Initial Balance',
                                validators=[validators.required()], 
                                render_kw={"placeholder": "10.00", "class": "form-control", "aria-describedby":"prependEuro"})
    submit = SubmitField(label='Add Account', render_kw={"class": "btn btn-primary"})