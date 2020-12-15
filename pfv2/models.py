from . import db


# class User(db.Model):
#     # primary keys are required by SQLAlchemy
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    acct_type = db.Column(db.String(100))
    balance = db.Column(db.String(100))


# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    month_balance = db.Column(db.String(100))
    year_balance = db.Column(db.String(100))


# class Incoming(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(100))
#     amount = db.Column(db.Numeric(100))
#     date = db.Column(db.DateTime)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     account_id = db.Column(db.Integer, db.ForeignKey('account.id'))


# class Expense(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(100))
#     amount = db.Column(db.Numeric(100))
#     date = db.Column(db.DateTime)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
