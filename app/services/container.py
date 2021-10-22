from typing import NoReturn

from app import injector, InitialSettings, app
from app.services.data_preparation_service import DataPreparationService
from app.services.history_service import HistoryService
from app.services.recommendation_service import RecommendationService


def container() -> NoReturn:
    """
    Dependency initialize container.
    Please do not change initialization order.
    """
    # Utils classes
    injector.map(init_settings=InitialSettings(app=app))

    # Services classes
    injector.map(data_preparation_service=DataPreparationService())
    injector.map(history_service=HistoryService())
    injector.map(recommendation_service=RecommendationService())
