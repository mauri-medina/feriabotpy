from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date, event
from sqlalchemy.orm import relationship

import db


class Holiday(db.Base):
    __tablename__ = 'holiday'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    message = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    celebrationDates = relationship("CelebrationDate", backref='holiday')

    def __init__(self, name, message, date):
        self.name = name
        self.message = message
        self.date = date


class CelebrationDate(db.Base):
    __tablename__ = "celebration_date"

    id = Column(Integer, primary_key=True)
    holiday_id = Column(Integer, ForeignKey("holiday.id"))
    date = Column(Date, nullable=False)
    celebration_date = Column(Date, nullable=True)

    @staticmethod
    def get_next_from_date(from_date):
        return db.session.query(CelebrationDate). \
            filter(CelebrationDate.date >= from_date). \
            order_by(CelebrationDate.date.asc()). \
            first()


@event.listens_for(CelebrationDate.__table__, 'after_create')  # it only runs once when the database doesn't yet exist
def init_db(*args, **kwargs):
    new_year = Holiday(name='Año nuevo', message='¡Feliz año nuevo!', date=get_date(1, 1, 2022))
    db.session.add(new_year)

    heroes_day = Holiday(name='Día de los heroes de la patria', message='Feliz día a los heroes de la patria',
                         date=get_date(1, 3, 2022))
    db.session.add(heroes_day)

    holy_thursday = Holiday(name='Jueves Santo', message='Muchas bendiciones en este jueves santo',
                            date=get_date(14, 4, 2022))
    db.session.add(holy_thursday)

    holy_friday = Holiday(name='Viernes Santo', message='Muchas bendiciones en este viernes santo',
                          date=get_date(15, 4, 2022))
    db.session.add(holy_friday)

    labor_day = Holiday(name='Día del trabajador', message='¡Feliz día del trabajador!', date=get_date(1, 5, 2022))
    db.session.add(labor_day)

    independence_day = Holiday(name='Día de de la independecia', message='¡Feliz día de la Independencia!',
                               date=get_date(14, 5, 2022))
    db.session.add(independence_day)

    independence_mother_day = Holiday(name='Día de de la independecia y Dia de la madre',
                                      message='¡Feliz día a todas las madres!', date=get_date(15, 5, 2022))
    db.session.add(independence_mother_day)

    chaco_peace_day = Holiday(name='Día de la Paz del Chaco', message='¡Feliz Día de la Paz del Chaco!',
                              date=get_date(12, 6, 2022))
    db.session.add(chaco_peace_day)

    asuncion_fundation = Holiday(name='Fundación de Asunción', message='¡Feliz Día de la Fundación de Asunción!',
                                 date=get_date(15, 8, 2022))
    db.session.add(asuncion_fundation)

    boqueron_victory = Holiday(name='Victoria de Boquerón', message='¡Feliz Día de la Victoria de Boquerón!',
                               date=get_date(29, 9, 2022))
    db.session.add(boqueron_victory)

    virgin_day = Holiday(name='Día de la Virgen de Caacupé', message='¡Feliz Día de la Virgen de Caacupé!',
                         date=get_date(8, 12, 2022))
    db.session.add(virgin_day)

    christmas = Holiday(name='Navidad', message='¡Feliz Navidad!', date=get_date(25, 12, 2022))
    db.session.add(christmas)

    census_day = Holiday(name='Censo Nacional', message='Hoy se realiza el censo nacional, a quedarse todos en casa', date=get_date(9, 11, 2022))
    db.session.add(census_day)

    db.session.commit()

    # 2022
    db.session.add(CelebrationDate(holiday=new_year, date=get_date(1, 1, 2022)))
    db.session.add(CelebrationDate(holiday=heroes_day, date=get_date(1, 3, 2022)))
    db.session.add(CelebrationDate(holiday=holy_thursday, date=get_date(14, 4, 2022)))
    db.session.add(CelebrationDate(holiday=holy_friday, date=get_date(15, 4, 2022)))
    db.session.add(CelebrationDate(holiday=labor_day, date=get_date(2, 5, 2022)))
    db.session.add(CelebrationDate(holiday=independence_day, date=get_date(14, 5, 2022)))
    db.session.add(CelebrationDate(holiday=independence_mother_day, date=get_date(15, 5, 2022)))
    db.session.add(CelebrationDate(holiday=chaco_peace_day, date=get_date(12, 6, 2022)))
    db.session.add(CelebrationDate(holiday=asuncion_fundation, date=get_date(15, 8, 2022)))
    db.session.add(CelebrationDate(holiday=boqueron_victory, date=get_date(3, 10, 2022)))
    db.session.add(CelebrationDate(holiday=census_day, date=get_date(9, 11, 2022)))
    db.session.add(CelebrationDate(holiday=virgin_day, date=get_date(8, 12, 2022)))
    db.session.add(CelebrationDate(holiday=christmas, date=get_date(25, 12, 2022)))

    # 2023
    db.session.add(CelebrationDate(holiday=new_year, date=get_date(1, 1, 2023)))
    db.session.add(CelebrationDate(holiday=heroes_day, date=get_date(27, 2, 2023)))
    db.session.add(CelebrationDate(holiday=holy_thursday, date=get_date(6, 4, 2023)))
    db.session.add(CelebrationDate(holiday=holy_friday, date=get_date(7, 4, 2023)))
    db.session.add(CelebrationDate(holiday=labor_day, date=get_date(1, 5, 2023)))
    db.session.add(CelebrationDate(holiday=independence_day, date=get_date(14, 5, 2023)))
    db.session.add(CelebrationDate(holiday=independence_mother_day, date=get_date(15, 5, 2023)))
    db.session.add(CelebrationDate(holiday=chaco_peace_day, date=get_date(12, 6, 2023)))
    db.session.add(CelebrationDate(holiday=asuncion_fundation, date=get_date(15, 8, 2023)))
    db.session.add(CelebrationDate(holiday=boqueron_victory, date=get_date(29, 9, 2023)))
    db.session.add(CelebrationDate(holiday=virgin_day, date=get_date(8, 12, 2023)))
    db.session.add(CelebrationDate(holiday=christmas, date=get_date(25, 12, 2023)))

    # 2024
    db.session.add(CelebrationDate(holiday=new_year, date=get_date(1, 1, 2024)))
    db.session.add(CelebrationDate(holiday=heroes_day, date=get_date(1, 3, 2024)))
    db.session.add(CelebrationDate(holiday=holy_thursday, date=get_date(28, 3, 2024)))
    db.session.add(CelebrationDate(holiday=holy_friday, date=get_date(29, 3, 2024)))
    db.session.add(CelebrationDate(holiday=labor_day, date=get_date(1, 5, 2024)))
    db.session.add(CelebrationDate(holiday=independence_day, date=get_date(14, 5, 2024)))
    db.session.add(CelebrationDate(holiday=independence_mother_day, date=get_date(15, 5, 2024)))
    db.session.add(CelebrationDate(holiday=independence_mother_day, date=get_date(15, 5, 2024)))
    db.session.add(CelebrationDate(holiday=chaco_peace_day, date=get_date(10, 6, 2024)))
    db.session.add(CelebrationDate(holiday=asuncion_fundation, date=get_date(15, 8, 2024)))
    db.session.add(CelebrationDate(holiday=boqueron_victory, date=get_date(29, 9, 2024)))
    db.session.add(CelebrationDate(holiday=virgin_day, date=get_date(8, 12, 2024)))
    db.session.add(CelebrationDate(holiday=christmas, date=get_date(25, 12, 2024)))

    # 2025
    db.session.add(CelebrationDate(holiday=new_year, date=get_date(1, 1, 2025)))

    db.session.commit()


def get_date(day: int, month: int, year: int) -> Date:
    return datetime.strptime(f'{day}-{month}-{year}', '%d-%m-%Y').date()
