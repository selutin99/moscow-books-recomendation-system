import pandas as pd

from app import pymysql_db
from config.queries import Queries


class DataPreparationService:
    def __init__(self):
        self.__offset_data = 10_000

    def get_unique_attributes(self):
        current_offset = 0
        global_data_frame: pd.DataFrame = pd.DataFrame()
        books_total_count, = pymysql_db.get_query(query=Queries.GET_BOOKS_COUNT)[0].values()
        total_offset_size: int = books_total_count // self.__offset_data

        for batch in range(total_offset_size):
            offset_dataframe = pd.read_sql(
                ('SELECT * FROM moscow_books.book LIMIT %s OFFSET %s' % (self.__offset_data, current_offset)),
                con=pymysql_db.connection
            )
            normalized_attributes: list = self.__calculate_value_counts(dataframe=offset_dataframe)
            # TODO write into books_converted table normalized attributes
            current_offset += self.__offset_data

    def __calculate_value_counts(self, dataframe: pd.DataFrame) -> list:
        normalized_result_attributes = list()

        # Get unique attributes
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().place.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().publ.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().yea.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().lan.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().serial.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().material.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().biblevel.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().ager.value_counts()))

        return normalized_result_attributes

    def __normalize_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())
