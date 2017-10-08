import pandas as pd
import datetime
import numpy as np
from itertools import cycle, dropwhile, takewhile, chain, accumulate

pd.options.display.width = 1000
pd.options.display.max_rows = 10


def produce_hu_au_years(build_year, start_year, end_year):
    hu_chain = accumulate(chain([build_year], [3], cycle([2])))
    return list(dropwhile(lambda y: y < start_year, takewhile(lambda x: x <= end_year, hu_chain)))

produce_hu_au_years(2017, 2017, 2025)


def hu_au(cars, years):
    year_now = datetime.date.today().year
    cars = cars.assign(end_year=lambda df: len(produce_hu_au_years(df.build_year, year_now, year_now+years)))
    np.array(cars.build_year, cars.end_year)



def fixed_expences(cars, years):
    return hu_au(cars, years) + insurance(cars) + tax(cars)


def running_expences(cars):
    return gas(cars) + oil_change(cars) + tires_change(cars) + repair_shop(cars)


def yearly_car_expences(cars, years):
    return fixed_expences(cars, years)+running_expences(cars)


cars = pd.read_csv("data.csv")
yearly_car_expences(cars, 10)