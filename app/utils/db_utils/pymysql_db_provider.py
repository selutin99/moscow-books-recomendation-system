from typing import NoReturn, Type

import pymysql

from app.config.profiles import Config


class PyMySQLProvider:

    def __init__(self, active_profile: Type[Config]):
        self.connection = pymysql.connect(
            host=active_profile.MYSQL_URL,
            user=active_profile.MYSQL_USER,
            password=active_profile.MYSQL_PASSWORD,
            database=active_profile.MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_query(self, query: str, params: tuple = ()) -> list:
        with self.connection.cursor() as cursor:
            # Read a record
            sql: str = query
            cursor.execute(sql, params)
            result = cursor.fetchall()
            self.connection.commit()
            return result

    def upsert_query(self, query: str, params: tuple = ()) -> NoReturn:
        with self.connection.cursor() as cursor:
            sql: str = query
            cursor.execute(sql, params)
        self.connection.commit()
