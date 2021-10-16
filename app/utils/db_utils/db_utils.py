from typing import NoReturn

from app import pymysql_db, db


def sync_commit() -> NoReturn:
    """
    Function required to maintain database consistency
    """
    db.session.commit()
    pymysql_db.connection.commit()
