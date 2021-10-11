from flask import jsonify, make_response
from flask import render_template, Blueprint

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/json')
def json():
    return make_response(jsonify(response='Hello world'), 200)
