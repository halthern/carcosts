import pandas as pd
import datetime
from itertools import cycle, dropwhile, takewhile, chain, accumulate

pd.options.display.width = 1000
pd.options.display.max_rows = 10

HU_AU_COST = 100
INSURANCE_COST = 500
RUN = 15000
OIL_CHANGE_INTERVAL = 15000
GAS_PRICE = 1.5


def produce_hu_au_years(build_year, start_year, end_year):
    hu_chain = accumulate(chain([build_year], [3], cycle([2])))
    return list(dropwhile(lambda y: y < start_year, takewhile(lambda x: x <= end_year, hu_chain)))


def hu_au(cars, years):
    year_now = datetime.date.today().year
    return cars.build_year.apply(lambda val: len(produce_hu_au_years(val, year_now, year_now+years))) * HU_AU_COST / years


def insurance(cars):
    return INSURANCE_COST


def hubraum_tax(cars):
    return cars.hubraum*10*2


def co2_tax(cars):
    return (cars.co2-95)*2


def tax(cars):
    return hubraum_tax(cars)+co2_tax(cars)


def fixed_expences(cars, years):
    return hu_au(cars, years) + insurance(cars) + tax(cars)


def gas(cars):
    return cars.mileage_mixed*RUN/100


def parking():
    return 2 * 2 * 12 + 1 * 10 * 12


def oil_change_work(cars):
    return 120


def oil_filter(cars):
    return 20


def oil(cars):
    return 20


def oil_change_materials(cars):
    return oil_filter(cars)+oil(cars)


def oil_change(cars):
    return (oil_change_work(cars) + oil_change_materials(cars))*RUN/OIL_CHANGE_INTERVAL


def tires_change(cars):
    return (10+10)*2


def repair_shop(cars):
    return 0


def running_expences(cars):
    return gas(cars) + oil_change(cars) + tires_change(cars) + repair_shop(cars) + parking()


def yearly_car_expences(cars, years):
    return fixed_expences(cars, years)+running_expences(cars)


cars = pd.read_csv("data.csv")
yearly_car_expences(cars, 10)/12