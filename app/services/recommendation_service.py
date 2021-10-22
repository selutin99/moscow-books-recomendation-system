import random

from app import pymysql_db
from app.config.queries import Queries


class RecommendationService:
    def __init__(self):
        self.__nearest_coefficient = 0.05

    def get_recommendations(self, history_books: list) -> list:
        ids_list: list = [book.get('id') for book in history_books]
        coefficient_dict: dict = {}
        recommended_result_list: list = []

        # Find history books coefficients
        for id in ids_list:
            book_coefficient = pymysql_db.get_query(Queries.FIND_BOOK_COEFFICIENT, tuple([id]))[0].get('summary')
            if book_coefficient:
                coefficient_dict[id] = book_coefficient
        # Find nearest books
        for id, coefficient in coefficient_dict.items():
            rec_book_coefficients: list = pymysql_db.get_query(Queries.FIND_NEAREST_BOOK, tuple([id]))
            for book_dict in rec_book_coefficients:
                recommended_coefficient = book_dict.get('summary')
                if abs(coefficient - recommended_coefficient) < self.__nearest_coefficient:
                    reco_book = pymysql_db.get_query(Queries.GET_BOOK, tuple([book_dict.get('recId')]))[0]
                    if reco_book not in history_books and reco_book not in recommended_result_list:
                        recommended_result_list.append(reco_book)
                    break
        return recommended_result_list

    def get_recommendations_for_newcomer(self):
        return pymysql_db.get_query(Queries.GET_BOOK_NEWCOMER, tuple([random.randint(1, 10000)]))
