import string
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Holiday:
    name: string
    message: string
    date: datetime.date


def load_holidays():
    global __holidays_list
    __holidays_list = sorted(__holidays_list, key=lambda h: h["date"])

    temp = []
    [temp.append(Holiday(**h)) for h in __holidays_list]
    __holidays_list = temp


def get_next_holiday(date: datetime) -> Holiday:
    return next(h for h in __holidays_list if h.date >= date)


def set_date(day: int, month: int, year: int) -> datetime.date:
    return datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y").date()


__holidays_list = [
    {
        "name": "Año nuevo", "message":
        "¡Feliz año nuevo!",
        "date": set_date(1, 1, 2022),
    },
    {
        "name": "Día de los heroes de la patria",
        "message": "¡Feliz día a los heroes de la patria",
        "date": set_date(1, 3, 2022),
    },
    {
        "name": "Jueves Santo",
        "message": "¡Muchas bendiciones en este jueves santo!",
        "date": set_date(14, 4, 2022),
    },
    {
        "name": "Viernes Santo",
        "message": "¡Muchas bendiciones en este viernes santo!",
        "date": set_date(15, 4, 2022),
    },
    {
        "name": "Día del trabajador",
        "message": "¡Feliz día del trabajador!",
        "date": set_date(1, 5, 2022),
    },
    {
        "name": "Día de de la independecia",
        "message": "¡Feliz día de la Independencia!",
        "date": set_date(14, 5, 2022),
    },
    {
        "name": "Día de de la independecia y Dia de la madre",
        "message": "¡Feliz día a todas las madres!",
        "date": set_date(15, 5, 2022),
    },
    {
        "name": "Día de la Paz del Chaco",
        "message": "¡Feliz Día de la Paz del Chaco!",
        "date": set_date(12, 6, 2022),
    },
    {
        "name": "Fundación de Asunción",
        "message": "¡Feliz Día de la Fundación de Asunción!",
        "date": set_date(15, 8, 2022),
    },
    {
        "name": "Victoria de Boquerón",
        "message": "¡Feliz Día de la Victoria de Boquerón!",
        "date": set_date(29, 9, 2022),
    },
    {
        "name": "Censo Nacional",
        "message": "¡Feliz año nuevo!",
        "date": set_date(9, 11, 2022),
    },
    {
        "name": "Día de la Virgen de Caacupé",
        "message": "¡Feliz Día de la Virgen de Caacupé!",
        "date": set_date(8, 12, 2022),
    },
    {
        "name": "Navidad",
        "message": "¡Feliz Navidad!",
        "date": set_date(25, 12, 2022),
    },
    {
        "name": "Año nuevo",
        "message": "¡Feliz año nuevo!",
        "date": set_date(1, 1, 2023),
    },
]
