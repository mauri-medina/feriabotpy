from datetime import date


class Holiday:
    def __init__(self, name: str, message: str, official_date: date, celebration_date: date = None) -> None:
        self.name = name
        self.message = message
        self.official_date = official_date
        self.celebration_date = celebration_date


def encode_holiday(h):
    if isinstance(h, Holiday):
        json_dict = {'name': h.name, 'message': h.message}

        str_official_date = None
        if h.official_date:
            str_official_date = str(h.official_date)
        json_dict['official_date'] = str_official_date

        str_celebration_date = None
        if h.celebration_date:
            str_celebration_date = str(h.celebration_date)
        json_dict['celebration_day'] = str_celebration_date

        return json_dict;