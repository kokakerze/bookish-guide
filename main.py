from collections import Counter, namedtuple
import re

from data import pushkin
from recordclass import RecordClass


def most_common(text):
    txt = text.lower()
    txt = txt.replace(' ', '')
    txt_format = re.sub(r'[^\w\s]', '', txt)
    counter = Counter(txt_format)
    return counter.most_common(5)


print(most_common(pushkin))

"""1st prt"""

Car = namedtuple('Car', [
    'manufacturer',
    'model',
    'length',
    'width',
    'height',
    'bhp',
    'acceleration',
    'consumption'])

car2 = Car("BMW", "550", 4972, 1868, 1467, 530, 3.8, 10.7)
car3 = Car("BMW", "X4M", 4578, 1927, 1620, 510, 4.1, 10.5)
car4 = Car("MERCEDES", "C63AMG", 4750, 1877, 1400, 510, 4.0, 8.6)
car5 = Car("MERCEDES", "GLE 63AMG", 4819, 1936, 1796, 557, 4.3, 11.8)
car6 = Car("LEXUS", "RX 350", 4890, 1895, 1705, 300, 8.2, 9)
car1 = Car("LEXUS", "ES", 4976, 1864, 1445, 249, 7.9, 12.6)

"""2nd prt"""

all_car = [car1, car2, car3, car4, car5, car6]


# all_car.sort([5])
# most_height = max([i.height for i in all_car])
# for i in all_car:
#     if i.height == most_height:
#         print(i)

def get_height(all_car):
    return all_car.height


def get_acceleration(all_car):
    return all_car.acceleration


all_car.sort(key=get_height, reverse=True)
most_height_cars = all_car.copy()
print(f"Most highest cars is : {most_height_cars[:3]}")

all_car.sort(key=get_acceleration)
best_dynamic_cars = all_car.copy()
print(f"Most dynamic cars is : {best_dynamic_cars[:3]}")

"""3rd prt"""


class Cars(RecordClass):
    manufacturer: str
    model: str
    length: int
    width: int
    height: int
    bhp: int
    acceleration: float
    consumption: float


car1_list = list(best_dynamic_cars[0])
car2_list = list(best_dynamic_cars[1])
car3_list = list(best_dynamic_cars[2])
car4_list = list(best_dynamic_cars[3])
car5_list = list(best_dynamic_cars[4])
car6_list = list(best_dynamic_cars[5])

car1 = Cars(manufacturer=car1_list[0], model=car1_list[1], length=car1_list[2], width=car1_list[3], height=car1_list[4],
            bhp=car1_list[5], acceleration=car1_list[6], consumption=car1_list[7])
car2 = Cars(manufacturer=car2_list[0], model=car2_list[1], length=car2_list[2], width=car2_list[3], height=car2_list[4],
            bhp=car2_list[5], acceleration=car2_list[6], consumption=car2_list[7])
car3 = Cars(manufacturer=car3_list[0], model=car3_list[1], length=car3_list[2], width=car3_list[3], height=car3_list[4],
            bhp=car3_list[5], acceleration=car3_list[6], consumption=car3_list[7])
car4 = Cars(manufacturer=car4_list[0], model=car4_list[1], length=car4_list[2], width=car4_list[3], height=car4_list[4],
            bhp=car4_list[5], acceleration=car4_list[6], consumption=car4_list[7])
car5 = Cars(manufacturer=car5_list[0], model=car5_list[1], length=car5_list[2], width=car5_list[3], height=car5_list[4],
            bhp=car5_list[5], acceleration=car5_list[6], consumption=car5_list[7])
car6 = Cars(manufacturer=car6_list[0], model=car6_list[1], length=car6_list[2], width=car6_list[3], height=car6_list[4],
            bhp=car6_list[5], acceleration=car6_list[6], consumption=car6_list[7])

all_cars2 = [car1, car2, car3, car4, car5, car6]


def tuning_center(car):
    bhp_pro = car.bhp * (1 + 10 / 100)
    return bhp_pro


for i in all_cars2[:3]:
    i.bhp = tuning_center(i)

print(all_cars2)

"""4th part"""
from dataclasses import dataclass


@dataclass
class Cars2:
    manufacturer: str
    model: str
    length: int
    width: int
    height: int
    bhp: int
    acceleration: float
    consumption: float


car1 = Cars2(manufacturer=car1_list[0], model=car1_list[1], length=car1_list[2], width=car1_list[3],
             height=car1_list[4],
             bhp=car1_list[5], acceleration=car1_list[6], consumption=car1_list[7])
car2 = Cars2(manufacturer=car2_list[0], model=car2_list[1], length=car2_list[2], width=car2_list[3],
             height=car2_list[4],
             bhp=car2_list[5], acceleration=car2_list[6], consumption=car2_list[7])
car3 = Cars2(manufacturer=car3_list[0], model=car3_list[1], length=car3_list[2], width=car3_list[3],
             height=car3_list[4],
             bhp=car3_list[5], acceleration=car3_list[6], consumption=car3_list[7])
car4 = Cars2(manufacturer=car4_list[0], model=car4_list[1], length=car4_list[2], width=car4_list[3],
             height=car4_list[4],
             bhp=car4_list[5], acceleration=car4_list[6], consumption=car4_list[7])
car5 = Cars2(manufacturer=car5_list[0], model=car5_list[1], length=car5_list[2], width=car5_list[3],
             height=car5_list[4],
             bhp=car5_list[5], acceleration=car5_list[6], consumption=car5_list[7])
car6 = Cars2(manufacturer=car6_list[0], model=car6_list[1], length=car6_list[2], width=car6_list[3],
             height=car6_list[4],
             bhp=car6_list[5], acceleration=car6_list[6], consumption=car6_list[7])

all_cars2 = [car1, car2, car3, car4, car5, car6]


def km2miles(car):
    miles_per_gallon = 235.22 / car.consumption
    miles_per_gallon = round(miles_per_gallon, 2)
    return miles_per_gallon


for i in all_cars2:
    i.consumption = km2miles(i)
print(all_cars2)

"""5th part"""

from itertools import combinations_with_replacement

combinations = list(combinations_with_replacement('123456', 2))
sum_combinations = []
for m in range(len(combinations)):
    sum = int(combinations[m][0]) + int(combinations[m][1])
    sum_combinations.append(sum)
counter = Counter(sum_combinations)
print(counter.most_common(3))
"""6th part"""

import numpy as np


def convert_num(num):
    return -float(num) if float(num) < 3.0 else num


data = np.loadtxt("iris.data", delimiter=",", usecols=(0, 1, 2, 3),
                  converters={0: convert_num, 1: convert_num, 2: convert_num, 3: convert_num})
print(data)