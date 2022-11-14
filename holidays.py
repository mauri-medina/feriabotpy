import json
import os
import string

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Holiday:
    name: string
    message: string
    date: string

    def __post_init__(self):
        self.date = datetime.strptime(self.date, "%d-%m-%Y").date()


def __get_from_json():
    with open(os.getenv('JSON_FILE') or "data.json") as json_file:
        data = json.load(json_file)
        temp = []
        [temp.append(Holiday(**i)) for i in data]
        return (temp)


def get_next_holiday(date: datetime) -> Holiday:
    return next(h for h in __get_from_json() if h.date >= date)
