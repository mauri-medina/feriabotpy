import json
import os

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Holiday:
    name: str
    message: str
    date: str

    def __post_init__(self):
        self.date = datetime.strptime(self.date, "%d-%m-%Y").date()


def __get_from_json() -> list:
    with open(os.getenv('JSON_FILE') or "data.json") as json_file:
        data = json.load(json_file)

        temp = []
        [temp.append(Holiday(**i)) for i in data]
        temp.sort(key=lambda h: h.date)

        return (temp)


def get_next_holiday(date: datetime) -> Holiday:
    return next(h for h in __get_from_json() if h.date >= date)
