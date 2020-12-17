from flask import Blueprint, render_template, request, jsonify
# Testing the wtforms 
from pfv2.forms import TestForm
# from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')

#### Test and Debug Views ###
@views.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm()
    return render_template('testform.html', form=form)

@views.route("/debug", methods=['GET', 'POST'])
def debug():
    data = request.form
    #data = request.args
    return jsonify(data)
