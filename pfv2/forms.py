from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


# class TestForm(FlaskForm):
#     account = StringField('Account', validators=[DataRequired()])
#     account_type = SelectField('Account Type', choices=[('savings', "Savings"), ('checking', 'Checking')])
#     submit = SubmitField('Create Account')

class AddAccountType(FlaskForm):
    account_type = StringField(label='Account Type', validators=[DataRequired()], 
                                render_kw={"placeholder": "Checking", "class": "form-control", "size": 30})
    submit = SubmitField(label='Add Account', render_kw={"class": "btn btn-primary"})
