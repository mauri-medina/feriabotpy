from datetime import date
from app.dao import dao
from app.model.holiday import Holiday


def get_all_holidays_in_year(year: int = date.today().year) -> list:
    if is_year_register(year):
        holidays = dao.get_holidays_for_year(year)
        holidays.sort(key=lambda day: day.official_date)  # sort holidays by official dates
        return holidays
    else:
        # TODO throw exception
        pass


def get_holiday_closest_to_date(from_date: 'date' = date.today()) -> Holiday:
    holidays = get_all_holidays_in_year(from_date.year)
    for holiday in holidays:
        if holiday.official_date >= from_date:
            return holiday

    # there are no more holidays left this year,
        # return first holiday from next year
    holidays = get_all_holidays_in_year(from_date.year + 1)
    return holidays[0]


def get_resgistered_years() -> list:
    return dao.get_registered_years()


def is_year_register(year: int) -> bool:
    years = get_resgistered_years()
    return year in years
