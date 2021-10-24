class ScheduledService:
    """
    Service not include in DI container
    because it contains only static methods
    """

    @staticmethod
    def keep_db_connection():
        # Get service from DI container
        from app import pymysql_db, db
        from datetime import datetime

        pmdb = pymysql_db
        sadb = db

        pmdb.get_query("SELECT * FROM moscow_books.book WHERE 1=1 LIMIT 1;")
        print('Scheduled done: ' + str(datetime.now()))
