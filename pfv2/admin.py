from flask import Blueprint, render_template, request, redirect, url_for, flash, redirect
from .models import Account
from . import db


admin = Blueprint('admin', __name__)


@admin.route('/admin')
def adm_interface():
    return render_template('admin.html')


@admin.route('/admin/accounts', methods=['GET', 'POST'])
@admin.route('/admin/accounts/<op>', methods=['GET', 'POST'])
@admin.route('/admin/accounts/<op>/<int:id>', methods=['GET', 'POST'])
def adm_accounts(op=None, id=None):
    if request.method == 'POST':
        if op is None:
            acct_name = request.form['accountName']
            acct_type = request.form['accountType']
            acct_balance = request.form['accountBalance']

            new_account = Account(name=acct_name,
                                  acct_type=acct_type,
                                  balance=acct_balance)
            db.session.add(new_account)
            db.session.commit()
            flash('Account added', 'success')
            return redirect(url_for('admin.adm_accounts'))

        elif op == "save":
            acct_name = request.form['accountName']
            acct_type = request.form['accountType']
            acct_balance = request.form['accountBalance']

            update_account = Account.query.filter_by(id=id).first()
            update_account.name = acct_name
            update_account.acct_type = acct_type
            update_account.balance = acct_balance
            db.session.commit()
            flash('Account Modified', 'success')
            return redirect(url_for('admin.adm_accounts'))
    else:
        if op == "remove":
            Account.query.filter_by(id=id).delete()
            db.session.commit()
            flash('Account Removed', 'critical')
            return redirect(url_for('admin.adm_accounts'))
        elif op == "edit":
            edit_account = Account.query.filter_by(id=id).first()
            return render_template('edit_account.html', account=edit_account)
        else:
            return render_template('accounts.html', accounts=Account.query.all())


@admin.route('/admin/budgets', methods=['GET', 'POST'])
def adm_budgets():
    return render_template('budgets.html')

@admin.route('/admin/categories', methods=['GET', 'POST'])
def adm_categories():
    return render_template('categories.html')
