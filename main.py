import datetime
import locale

import tweepy

import db
from models import Holiday, CelebrationDate
from config import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, SECRET_ACCESS_TOKEN


def run():
    today = datetime.date.today()
    next_holiday = CelebrationDate.get_next_from_date(today)
    if next_holiday.date == today:
        message = f"{next_holiday.holiday.message}"
        tweet(message)

        tomorrow = today + datetime.timedelta(days=10)
        next_holiday = CelebrationDate.get_next_from_date(tomorrow)

    days_to_holiday = (next_holiday.date - today).days
    message = ""
    if days_to_holiday == 1:
        message = 'Falta 1 dia para el siguiente feriado\n'
    else:
        message = f'Faltan {days_to_holiday} dias para el siguiente feriado\n'

    message += f'Feriado: {next_holiday.holiday.name}\n'
    message += """Fecha: {0} {1} de {2}""".format(
        next_holiday.date.strftime('%A'),  # weekday
        next_holiday.date.strftime('%d'),  # day of month
        next_holiday.date.strftime('%B'),  # month name
    )

    tweet(message)


def tweet(message: str) -> None:
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)
    print(message)
    # api = tweepy.API(auth)
    # api.update_status(message)


if __name__ == '__main__':
    # we want month and days names in spanish
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    db.Base.metadata.create_all(db.engine)
    run()
