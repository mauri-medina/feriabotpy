from datetime import date, datetime, timedelta
import tweepy
import locale
from app.model import holiday
from app.service import service
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def tweet(message: str) -> None:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(message)


def get_next_holiday_from_date(from_date: date = date.today()) -> holiday:
    return service.get_holiday_closest_to_date(from_date)


def date_to_human(date_to_convert: date) -> str:
    return """{0} {1} de {2}""".format(
        date_to_convert.strftime('%A'),  # day name
        date_to_convert.strftime('%d'),  # day of month
        date_to_convert.strftime('%B'))  # month name


def tweet_next_holiday(from_date: date) -> None:
    holiday = get_next_holiday_from_date(from_date)

    official_date = holiday.official_date
    celebration_date = holiday.celebration_date
    now = datetime.now().date()

    # if holiday has not been moved to another day
    if not celebration_date:
        days_to_holiday = calculate_days_between_dates(now, official_date)
        if days_to_holiday == 0:
            message = 'Hoy se celebra el feriado: ' + holiday.name
            message += '\n' + holiday.message
            tweet(message)
            tweet_next_holiday(now + timedelta(days=1))
        elif days_to_holiday > 0:
            message = """{0} {1} {2} para el siguiente feriado""".format(
                'Falta' if days_to_holiday == 1 else 'Faltan',
                days_to_holiday,
                'dia' if days_to_holiday == 1 else 'dias')

            message += '\nFeriado: ' + holiday.name
            message += '\nFecha: ' + date_to_human(official_date)
            tweet(message)
    else:
        days_to_celebration = calculate_days_between_dates(now, celebration_date)
        if days_to_celebration > 0:
            message = """{0} {1} {2} para el siguiente feriado""".format(
                'Falta' if days_to_celebration == 1 else 'Faltan',
                days_to_celebration,
                'dia' if days_to_celebration == 1 else 'dias')

            message += '\nFeriado: ' + holiday.name
            message += '\nFecha: ' + date_to_human(official_date)
            message += '\nSe pasa al: ' + date_to_human(celebration_date)
            tweet(message)
        else:
            if days_to_celebration == 0:
                message = 'Hoy se celebra el feriado: ' + holiday.name
                message += '\n' + holiday.message
                tweet(message)

            # check for the next holiday from the end of this holiday, in case that the holiday celebration date is
            # before that official date
            days_to_holiday_date = calculate_days_between_dates(
                now,
                celebration_date if celebration_date > official_date else official_date)

            tweet_next_holiday(now + timedelta(days=days_to_holiday_date + 1))


def calculate_days_between_dates(start_date: date, end_date: date) -> int:
    return (end_date - start_date).days


# we want month and days names in spanish
locale.setlocale(locale.LC_ALL, 'es_ES')
tweet_next_holiday(date.today())
