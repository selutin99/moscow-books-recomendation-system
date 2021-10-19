from flask import jsonify, make_response, request
from flask import render_template, Blueprint

from app.services.data_preparation_service import DataPreparationService
from app.utils.flask_inject import inject

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/data/prepare')
@inject('data_preparation_service')
def data_preparation(data_preparation_service: DataPreparationService):
    data_preparation_service.get_unique_attributes(
        is_parallel=True,
        offset=request.args.get('offset', type=int)
    )
    return make_response(jsonify(response='Data processed start successfully'), 200)
