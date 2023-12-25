import datetime
import locale
import os

import tweepy
from dotenv import load_dotenv

import db
from models import Holiday, CelebrationDate


def run():
    today = datetime.date.today()
    next_holiday = CelebrationDate.get_next_from_date(today)
    if next_holiday.date == today:
        message = f"{next_holiday.holiday.message}"
        tweet(message)

        tomorrow = today + datetime.timedelta(days=1)
        next_holiday = CelebrationDate.get_next_from_date(tomorrow)

    days_to_holiday = (next_holiday.date - today).days
    message = ""
    if days_to_holiday == 1:
        message = 'Mañana es Feriado! No se olviden de apagar sus alarmas\n'
    else:
        message = f'Faltan {days_to_holiday} dias para el siguiente feriado\n'

    message += f'Feriado: {next_holiday.holiday.name}\n'
    message += """Fecha: {0} {1} de {2}""".format(
        next_holiday.date.strftime('%A'),  # name of weekday
        next_holiday.date.strftime('%e'),  # day of month without leading zero
        next_holiday.date.strftime('%B'),  # month name
    )

    tweet(message)


def tweet(message: str) -> None:
    if os.getenv('DEBUG'):
        print(message)
        return

    client = tweepy.Client(
        os.getenv('BEARER_TOKEN'),
        os.getenv('API_KEY'),
        os.getenv('API_SECRET_KEY'),
        os.getenv('ACCESS_TOKEN'),
        os.getenv('SECRET_ACCESS_TOKEN')
    )

    print(message)
    client.create_tweet(text=message)


if __name__ == '__main__':
    # we want month and days names in spanish
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    load_dotenv()

    db.Base.metadata.create_all(db.engine)
    run()
