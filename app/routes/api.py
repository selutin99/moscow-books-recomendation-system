from flask import Blueprint, make_response, jsonify

from app.services.history_service import HistoryService
from app.utils.flask_inject import inject

api = Blueprint('api', __name__)


@api.route('/api/find/<int:user_id>')
@inject('history_service')
def list_of_recommendations(user_id: int, history_service: HistoryService):
    return make_response(jsonify(response='Hello world'), 200)
