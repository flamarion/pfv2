from flask import Blueprint, render_template, request, jsonify
# from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route("/debug", methods=['GET', 'POST'])
def debug():
    data = request.form
    return jsonify(data)
