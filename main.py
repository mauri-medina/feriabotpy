import datetime
import locale

from dotenv import load_dotenv

from holidays import get_next_holiday, load_holidays
from twitter import tweet


def run():
    today = datetime.date.today()
    next_holiday = get_next_holiday(today)

    if next_holiday == today:
        message = f"{next_holiday.message}"
        tweet(message)

        tomorrow = today + datetime.timedelta(days=10)
        next_holiday = get_next_holiday(tomorrow)

    days_to_holiday = (next_holiday.date - today).days
    if days_to_holiday == 1:
        message = "Mañana es Feriado! No se olviden de apagar sus alarmas\n"
    else:
        message = f"Faltan {days_to_holiday} dias para el siguiente feriado\n"

    message += f"Feriado: {next_holiday.name}\n"
    message += """Fecha: {0}{1} de {2}""".format(
        next_holiday.date.strftime("%A"),  # name of weekday
        next_holiday.date.strftime("%e"),  # day of month without leading zero
        next_holiday.date.strftime("%B"),  # month name
    )

    tweet(message)


if __name__ == "__main__":
    # we want month and days names in spanish
    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    load_dotenv()
    load_holidays()
    run()
