from typing import NoReturn

from app import pymysql_db


def sync_commit() -> NoReturn:
    """
    Function required to maintain database consistency
    """
    pymysql_db.connection.commit()
