import json

from flask import Blueprint
from werkzeug.wrappers import response

from app.services.history_service import HistoryService
from app.utils.flask_inject import inject

api = Blueprint('api', __name__)


@api.route('/api/find/<int:user_id>')
@inject('history_service')
def list_of_recommendations(user_id: int, history_service: HistoryService):
    history_list: list = history_service.generate_user_history(user_id=user_id)
    history_response: dict = {'history': history_list}
    response.content_type = 'application/json'
    return '<pre>{}</pre>'.format(json.dumps(history_response, indent=4, ensure_ascii=False, sort_keys=True, ))
