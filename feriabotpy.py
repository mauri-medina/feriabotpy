from datetime import datetime

import tweepy

from DBcm import UseDataBase
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


class Holiday:
    def __init__(self, id: int, name: str, celebrated_on: 'date', message: str) -> None:
        self.id = id
        self.name = name
        self.celebrated_on = celebrated_on
        self.message = message


def get_next_holiday(day_offset: int = 0):
    """Search and return the next holiday from the database"""
    with UseDataBase() as cursor:
        _SQL = """SELECT * FROM holiday WHERE celebrated_on >= curdate() ORDER BY celebrated_on ASC LIMIT %s, 1"""
        cursor.execute(_SQL, (day_offset,))
        result = cursor.fetchall()[0]

    return Holiday(result[0], result[1], result[2], result[3])


def tweet(message: str) -> None:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(message)


def switch_month(month: int) -> str:
    switcher = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciemnre'
    }
    return switcher.get(month, "Mes incorrecto")


def prepare_countdown_message(holiday: Holiday) -> str:
    delta_time = holiday.celebrated_on - datetime.now().date()
    days_left = delta_time.days

    return """Faltan {0} días para el próximo feriado\nFeriado: {1}\nFecha: {2} de {3}""".format(
        days_left, holiday.name, holiday.celebrated_on.day, switch_month(holiday.celebrated_on.month))


def prepare_is_holiday_day_message(holiday: Holiday) -> str:
    return """{0}""".format(holiday.message)


holiday = get_next_holiday()
if holiday.celebrated_on > datetime.today().date():  # holiday is not today
    tweet(prepare_countdown_message(holiday))
else:
    tweet(prepare_is_holiday_day_message(holiday))

    # show the next holiday from 1 day from today
    holiday = get_next_holiday(1)
    tweet(prepare_countdown_message(holiday))
