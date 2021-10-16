import pandas as pd
from sqlalchemy import create_engine

from app import pymysql_db
from config.queries import Queries


class DataPreparationService:
    def __init__(self):
        self.__offset_data = 10_000
        self.__engine = create_engine('mysql+pymysql://root:password@localhost/moscow_books')

    def get_unique_attributes(self, is_parallel: bool = False, offset: int = 0):
        current_offset: int = offset if offset else 0
        books_total_count, = pymysql_db.get_query(query=Queries.GET_BOOKS_COUNT)[0].values()
        total_offset_size: int = books_total_count // self.__offset_data

        for batch in range(total_offset_size):
            offset_dataframe = pd.read_sql(
                ('SELECT * FROM moscow_books.book LIMIT %s OFFSET %s' % (self.__offset_data, current_offset)),
                con=pymysql_db.connection
            )
            normalized_attributes: list = self.__calculate_normalized_values(dataframe=offset_dataframe)

            for index, offset_dataframe_value in offset_dataframe.iterrows():
                self.__numerify_dataframe(
                    normalized_attributes=normalized_attributes,
                    changed_dataframe=offset_dataframe_value
                )
                writed_dataframe: pd.DataFrame = pd.DataFrame(offset_dataframe_value).T
                writed_dataframe.to_sql(con=self.__engine, name='books_converted', if_exists='append', index=False)
                print('Convert row #', index + current_offset)

            if is_parallel:
                break
            current_offset += self.__offset_data

    def __calculate_normalized_values(self, dataframe: pd.DataFrame) -> list:
        normalized_result_attributes = list()

        # Get unique attributes
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().place.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().publ.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().yea.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().lan.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().rubrics.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().person.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().serial.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().material.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().biblevel.value_counts()))
        normalized_result_attributes.append(self.__normalize_dataframe(dataframe.drop_duplicates().ager.value_counts()))

        return normalized_result_attributes

    def __normalize_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())

    def __numerify_dataframe(self, normalized_attributes: list, changed_dataframe: pd.Series) -> pd.Series:
        changed_dataframe['place'] = normalized_attributes[0][changed_dataframe['place']]
        changed_dataframe['publ'] = normalized_attributes[1][changed_dataframe['publ']]
        changed_dataframe['yea'] = normalized_attributes[2][changed_dataframe['yea']]
        changed_dataframe['lan'] = normalized_attributes[3][changed_dataframe['lan']]
        changed_dataframe['rubrics'] = normalized_attributes[4][changed_dataframe['rubrics']]
        changed_dataframe['person'] = normalized_attributes[5][changed_dataframe['person']]
        changed_dataframe['serial'] = normalized_attributes[6][changed_dataframe['serial']]
        changed_dataframe['material'] = normalized_attributes[7][changed_dataframe['material']]
        changed_dataframe['biblevel'] = normalized_attributes[8][changed_dataframe['biblevel']]
        changed_dataframe['ager'] = normalized_attributes[9][changed_dataframe['ager']]

        return changed_dataframe


if __name__ == '__main__':
    service = DataPreparationService()
    service.get_unique_attributes(is_parallel=True, offset=int(input('Type offset: ')))
