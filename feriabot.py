from flask import Flask, request
import json
from app.service import service
from app.model.holiday import encode_holiday
from datetime import date, datetime

app = Flask(__name__)


@app.route('/feriado/anho/<year>')
def get_holidays_from_year(year: int = date.today().year) -> list:
    holidays = service.get_all_holidays_in_year(int(year))
    return convert_holidays_to_json(holidays)


@app.route('/feriado/anho/registrados')
def get_registered_years() -> list:
    """Return all the years that the holidays are register"""
    years = service.get_resgistered_years()
    return json.dumps(years, sort_keys=True)


@app.route('/feriado/proximo')
def get_next_holiday() -> str:
    """ Returns next holiday from today """
    from_date = request.args.get('desde_fecha', default=None)
    if from_date:
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
    else:
        from_date = date.today()

    holiday = service.get_holiday_closest_to_date(from_date)
    return convert_holidays_to_json(holiday)


def convert_holidays_to_json(holidays: list) -> str:
    return json.dumps(holidays, default=encode_holiday, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
