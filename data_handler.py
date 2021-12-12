"""CSC110 Fall 2021: Cryptographer - Data Handler

Module Description
==================
This module contains the dataclasses for individual points of a cryptocurrency and the dataset
that brings together multiple points.

It contains functions that read from the dataset found on kaggle by Sudlai Rajkumar and processes
each row in order to make the class objects.

Copyright and Usage Information
===============================
This file is intended exclusively for academic use for the University of Toronto St. George Campus
in the CSC110 class of Fall 2021. Any distribution of this code, with or without changes,
are expressly prohibited.

This file is Copyright (c) 2021 Madeline Ahn, and Samuel Weiss.
"""
import random
from dataclasses import dataclass
import datetime
import csv
import os


@dataclass
class Point:
    """A class containing information about one day of a cryptocurrency.

    Instance Attributes:
        - name: Name of the cryptocurrency.
        - date: Date for that day's high/low/marketcap for the cryptocurrency.
        - high: Highest value of the cryptocurrency that day.
        - low: Lowest value of the cryptocurrency that day.
        - marketcap: Total value of all the shares of the cryptocurrency that day.

    Representation Invariants:
        - self.name != ''
    """
    name: str
    date: datetime.date
    high: float
    low: float
    marketcap: int


@dataclass
class Dataset:
    """Class that brings together objects from Point that have the same cryptocurrency name.

    Instance Attributes:
        - points: a list of points in the dataset
        - color: colour of points in the dataset
        - name: name of the specific dataset (i.e. Bitcoin)

    Representation Invariants:
        - all((0 <= nums <= 255 for nums in self.color))
        - 8 >= len(name) > 0
        - self.name == self.points[0].name
    """
    points: list[Point]
    color: tuple[int, int, int]
    name: str


def create_datasets(path: str) -> dict[str, Dataset]:
    """Opens all of the csv files and creates a list of lists for each point.

    Sample Usage:
    >>> create_datasets('data')
    """
    color_assignments = {'Bitcoin': (250, 180, 10),
                         'Ethereum': (170, 190, 230),
                         'Dogecoin': (160, 140, 100),
                         'AAVE': (160, 100, 160),
                         'Litecoin': (60, 70, 120),
                         'BinanceCoin': (75, 75, 70),
                         'Cardano': (15, 40, 130),
                         'ChainLink': (40, 130, 200),
                         'Cosmos': (100, 40, 150),
                         'CryptocomCoin': (20, 60, 80),
                         'EOS': (180, 200, 220),
                         'Iota': (60, 130, 100),
                         'Monero': (220, 120, 50),
                         'NEM': (130, 220, 190),
                         'Polkadot': (220, 60, 190),
                         'Solana': (180, 120, 230),
                         'Stellar': (10, 210, 240),
                         'Tether': (45, 145, 120),
                         'Tron': (220, 30, 20),
                         'Uniswap': (200, 20, 100),
                         'USDCoin': (20, 80, 220),
                         'WrappedBitcoin': (120, 50, 210),
                         'XRP': (230, 240, 140)}
    datasets = {}
    for filename in os.listdir(path):  # Finds all the files in /data
        if filename.endswith('csv'):
            with open(f'{path}/{filename}') as file:  # opens all csv in /data
                reader = csv.reader(file)
                next(reader)  # Gains headers from this line if used in assignment.
                points = [process_row(row) for row in reader]
                if points[0].name in color_assignments:
                    color = color_assignments[points[0].name]
                else:
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                new_dataset = Dataset(points=points,
                                      color=color,
                                      name=points[0].name)
                datasets[new_dataset.name] = new_dataset
    return datasets


def process_row(row: list[str]) -> Point:
    """Process a row of data from a csv file.

    Note that we use the stock symbol as the name to keep names as short as possible.

    Preconditions:
      - row has the same format as the csv files found from kaggle found by us
    """
    if len(row[1]) < 9:
        name = row[1]
    else:
        name = row[2]
    return Point(name=name,
                 date=str_to_date(row[3]),
                 high=round(float(row[4]), 3),
                 low=round(float(row[5]), 3),
                 marketcap=int(round(float(row[9]))))


def str_to_date(date: str) -> datetime.date:
    """Convert a string in yyyy-mm-dd format to a datetime.date.

    Preconditions:
        - len(date_string) == 10
        - date_string[4] == '-'
        - date_string[8] == '-'
        - 13 > int(date[5:7]) > 0
        - 32 > int(date[8:10) > 0

    >>> str_to_date('2020-04-14')
    datetime.date(2020, 4, 14)
    """
    return datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'random', 'datetime', 'csv', 'os'],
        'allowed-io': ['create_datasets'],
        'disable': ['R1705', 'C0200'],
        'max-args': 7
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
