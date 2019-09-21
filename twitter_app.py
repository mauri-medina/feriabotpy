from datetime import date, datetime, timedelta
import tweepy
import locale
import feriabot
from app.model import holiday
from app.service import service
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def tweet(message: str) -> None:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    # api.update_status(message)

    print(message)


def get_next_holiday_from_date(from_date: date = date.today()) -> holiday:
    return service.get_holiday_closest_to_date()


def date_to_human(date_to_convert: date) -> str:
    return """{0} {1} de {2}""".format(
        date_to_convert.strftime('%A'),  # day name
        date_to_convert.strftime('%d'),  # day of month
        date_to_convert.strftime('%B'))  # month name


def form_days_to_holiday_message(holiday_date: date) -> str:
    delta_days = (holiday_date - date.today()).days
    return """{0} {1} {2} para el feriado""".format(
        'Falta' if delta_days == 1 else 'Faltan',
        delta_days,
        'dia' if delta_days == 1 else 'dias',
    )


def tweet_next_holiday(from_date: date) -> None:
    holiday = get_next_holiday_from_date(from_date)
    official_date = holiday.official_date

    celebration_date = holiday.celebration_date

    now = date.today()
    message = ''

    if official_date == now:
        message = holiday.message
        if celebration_date:
            message += '\nSe pasa al: ' + date_to_human(celebration_date)
            message += '\n' + form_days_to_holiday_message(celebration_date)
            tweet(message)
        else:
            tweet(message)
            tweet_next_holiday(now + timedelta(days=1))
    elif celebration_date and celebration_date == now:
        message += 'Hoy se celebra el feriado: ' + holiday.name
        message += '\n' + holiday.message
        tweet(message)
        tweet_next_holiday(now + timedelta(days=1))
    else:
        message = form_days_to_holiday_message(official_date)
        if celebration_date:
            message = form_days_to_holiday_message(celebration_date)

        message += '\nFeriado: ' + holiday.name
        message += '\nFecha: ' + date_to_human(official_date)
        if celebration_date:
            message += '\nSe pasa al: ' + date_to_human(celebration_date)
        tweet(message)


# we want month and days names in spanish
locale.setlocale(locale.LC_ALL, 'es_ES')
tweet_next_holiday(date.today())
