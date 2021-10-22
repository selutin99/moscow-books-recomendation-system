import json

from flask import Blueprint
from werkzeug.wrappers import response

from app.services.history_service import HistoryService
from app.services.recommendation_service import RecommendationService
from app.utils.flask_inject import inject

api = Blueprint('api', __name__)


@api.route('/api/find/new')
@inject('recommendation_service')
def list_of_recommendations_new(recommendation_service: RecommendationService):
    recommendation_response: dict = {'recommendations': recommendation_service.get_recommendations_for_newcomer()}
    response.content_type = 'application/json'
    return '<pre>{}</pre>'.format(
        json.dumps([recommendation_response, {'history': []}], indent=4, ensure_ascii=False, sort_keys=True, ))


@api.route('/api/find/<int:user_id>')
@inject('history_service', 'recommendation_service')
def list_of_recommendations(user_id: int,
                            history_service: HistoryService,
                            recommendation_service: RecommendationService):
    history_list: list = history_service.generate_user_history(user_id=user_id)
    recommendation_response: dict = {
        'recommendations': recommendation_service.get_recommendations(history_books=history_list)}
    history_response: dict = {'history': history_list}
    response.content_type = 'application/json'
    return '<pre>{}</pre>'.format(
        json.dumps([history_response, recommendation_response], indent=4, ensure_ascii=False, sort_keys=True, ))
