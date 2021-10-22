from app import pymysql_db
from app.config.queries import Queries


class HistoryService:
    def generate_user_history(self, user_id: int) -> list:
        history_list: list = list()

        book_ids_list = pymysql_db.get_query(Queries.GET_USER_HISTORY_BOOK_IDS, tuple([user_id]))
        for book_id in book_ids_list:
            book_id_value = book_id.get('catalogueRecordID')
            if book_id_value:
                history: list = pymysql_db.get_query(Queries.GET_BOOK, tuple([book_id_value]))
                for current_book in history:
                    if current_book not in history_list:
                        history_list.append(current_book)
        return history_list
