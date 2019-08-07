import datetime

import mysql.connector

from app.model.holiday import Holiday
from config import DB_CONFIG


class UseDataBase:
    """ContextManager for mysql operations"""

    def __init__(self) -> None:
        self.configuration = DB_CONFIG

    def __enter__(self) -> 'cursor':
        self.connection = mysql.connector.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


def get_holidays_for_year(year: int = datetime.datetime.now().year):
    """Search for all holidays in the specified year"""
    with UseDataBase() as cursor:
        _SQL = """SELECT h.name, h.message, h.`day`, h.`month`, h_date.`day` AS cel_day, h_date.`month` AS cel_month, %s AS cel_year 
                    FROM holiday AS h
	                    LEFT JOIN holiday_celebration_date AS h_date ON h.id = h_date.holiday_id AND h_date.`year` = %s"""
        cursor.execute(_SQL, (year, year,))
        result = cursor.fetchall()

    return extract_holidays_from_result(result)


def extract_holidays_from_result(result: list) -> []:
    holidays = []
    for row in result:
        name = row[0]
        message = row[1]
        year = row[-1]

        # official date
        official_day = row[2]
        official_month = row[3]
        official_date = None
        if official_day is not None and official_day > 0:  # Easter week dates are zero
            official_date = datetime.date(year, official_month, official_day)

        # celebration day
        celebration_day = row[4];
        celebration_month = row[5];
        celebration_date = None
        if celebration_day is not None:
            celebration_date = datetime.date(year, celebration_month, celebration_day)

        # Easter week should only have official dates
        if official_date is None:
            official_date = celebration_date
            celebration_date = None

        holidays.append(Holiday(name, message, official_date, celebration_date))

    return holidays


def get_registered_years() -> list:
    with UseDataBase() as cursor:
        _SQL = """SELECT DISTINCT `year` FROM holiday.holiday_celebration_date"""
        cursor.execute(_SQL)
        result = cursor.fetchall()

    years = []
    for year in result:
        years.append(year[0])

    return years

