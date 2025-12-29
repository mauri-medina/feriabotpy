import datetime
import os

import locale
import tweepy
from dotenv import load_dotenv
import requests
from datetime import date, datetime, timedelta

load_dotenv()
# google
calendar_id = os.getenv("GOOGLE_CALENDAR_ID")
google_api_key = os.getenv("GOOGLE_API_KEY")
# twitter
twitter_bearer_token = os.getenv("BEARER_TOKEN")
twitter_api_key = os.getenv("API_KEY")
twitter_api_secret_key = os.getenv("API_SECRET_KEY")
twitter_api_access_token = os.getenv("ACCESS_TOKEN")
twitter_api_secret_access_token = os.getenv("SECRET_ACCESS_TOKEN")


class Holiday:
    def __init__(self, name: str, message: str, date: datetime):
        self.name = name
        self.message = message
        self.date = date


def main():
    next_holiday = get_next_holiday()
    if next_holiday:
        today = datetime.today().date()

        if next_holiday.date.date() == today:
            tweet(next_holiday.message)
            tomorrow = today + timedelta(days=1)
            next_holiday = get_next_holiday(from_date=datetime.combine(tomorrow, datetime.min.time()))

        days_to_next_holiday = (next_holiday.date.date() - today).days
        message = ""

        if days_to_next_holiday == 1:
            message = "Mañana es Feriado! No se olviden de apagar sus alarmas\n"
        else:
            message = f"Faltan {days_to_next_holiday} días para el siguiente feriado\n"

        message += f"Feriado: {next_holiday.name}\n"
        message += """Fecha: {0} {1} de {2}""".format(
            next_holiday.date.strftime("%A"),  # name of weekday
            next_holiday.date.strftime("%e"),  # day of month without leading zero
            next_holiday.date.strftime("%B"),  # month name
        )

        tweet(message)


def get_next_holiday(from_date: date = datetime.now()):
    params = {
        "key": google_api_key,
        "timeMin": from_date.astimezone().isoformat(),
        "maxResults": 1,
        "orderBy": "startTime",
        "singleEvents": "true",
    }
    holiday = None
    response = requests.get(f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events", params=params)
    items = response.json().get("items", [])
    if items:
        item = items[0]
        holiday = Holiday(
            name=item.get("summary").strip(),
            message=item.get("description", "").strip(),
            date=datetime.fromisoformat(item.get("start").get("date")),
        )
    return holiday


def tweet(message: str) -> None:
    print(f"Message to tweet:\n{message}")
    if os.getenv("DEBUG"):
        print(message)
        return

    print("twitter_bearer_token: " + twitter_bearer_token)
    print("twitter_api_key: " + twitter_api_key)
    print("twitter_api_secret_key " + twitter_api_secret_key)
    print("twitter_api_access_token: " + twitter_api_access_token)
    print("twitter_api_secret_access_token: " + twitter_api_secret_access_token)

    client = tweepy.Client(
    consumer_key=twitter_api_key, 
    consumer_secret=twitter_api_secret_key,
    access_token=twitter_api_access_token, 
    access_token_secret=twitter_api_secret_access_token
)
    response = client.create_tweet(text=message)
    print(f"tweepy response -> {response}")


if __name__ == "__main__":
    # we want month and days names in Spanish
    locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
    main()
