from datetime import date, datetime, timedelta
import requests
import tweepy
import locale
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def tweet(message: str) -> None:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(message)

    print(message)


def get_next_holiday_from_date(from_date: date = date.today()) -> dict:
    url = 'http://127.0.0.1:5000/feriado/proximo'
    params = {'desde_fecha': from_date.strftime('%Y-%m-%d')}
    response = requests.get(url, params=params)
    return response.json()


def str_to_date(str_date: str) -> date:
    return datetime.strptime(str_date, '%Y-%m-%d').date()


def date_to_human(date_to_convert: date) -> str:
    return """{0} {1} de {2}""".format(
        date_to_convert.strftime('%A'),  # day name
        date_to_convert.strftime('%d'),  # day of month
        date_to_convert.strftime('%B'))  # month name


def get_celebration_date(holiday: dict) -> date:
    celebration_date = None
    if holiday['celebration_date']:
        celebration_date = str_to_date(holiday['celebration_date'])
    return celebration_date


def form_days_to_holiday_message(delta_days: str) -> str:
    return """{0} {1} {2}""".format(
        'Falta' if delta_days == 1 else 'Faltan',
        delta_days,
        'dia' if delta_days == 1 else 'dias',
    )


def tweet_next_holiday(from_date: date) -> None:
    holiday_json = get_next_holiday_from_date(from_date)
    official_date = str_to_date(holiday_json['official_date'])

    celebration_date = get_celebration_date(holiday_json)
    if holiday_json['celebration_date']:
        celebration_date = str_to_date(holiday_json['celebration_date'])

    now = date.today()
    message = ''

    if official_date == now:
        message = holiday_json['message']
        if celebration_date:
            message += '\nSe pasa al: ' + date_to_human(celebration_date)
            delta_days = celebration_date - now
            message += '\n' + form_days_to_holiday_message(delta_days.days)
            tweet(message)
        else:
            tweet(message)
            tweet_next_holiday(now + timedelta(days=1))
    elif celebration_date and celebration_date == now:
        message = 'Hoy se celebra el feriado: ' + holiday_json['name']
        message += '\n' + holiday_json['message']
        tweet(message)
        tweet_next_holiday(now + timedelta(days=1))
    else:
        message = 'Feriado: ' + holiday_json['name']
        message += '\nFecha: ' + date_to_human(official_date)
        delta_days = official_date - now
        if celebration_date:
            message += '\nSe pasa al: ' + date_to_human(celebration_date)
            delta_days = celebration_date - now
        message += '\n' + form_days_to_holiday_message(delta_days.days)
        tweet(message)


# we want month and days names in spanish
locale.setlocale(locale.LC_ALL, 'es_ES')
tweet_next_holiday(date.today())
