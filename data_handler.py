"""CSC110: Cryptographer

TODO: DOCSTRING, Copyright things
"""

# Import functions
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
    High: float
    Low: float
    Marketcap: int


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
    # TODO add other colours for all currencies
    color_assignments = {'Bitcoin': (250, 180, 10),
                         'Ethereum': (170, 190, 230),
                         'Dogecoin': (160, 140, 100),
                         'AAVE': (160, 100, 160),
                         'Litecoin': (60, 70, 120)}
    datasets = {}
    for filename in os.listdir(path):  # finds all the files in /data
        if filename.endswith('csv'):
            with open(f'{path}/{filename}') as file:  # opens all csv in /data
                reader = csv.reader(file)
                next(reader)  # can gain headers from this line if used in assignment
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
                 High=round(float(row[4]), 3),
                 Low=round(float(row[5]), 3),
                 Marketcap=int(round(float(row[9]))))


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
        'allowed-io': ['open'],
        'disable': ['R1705', 'C0200'],
        'max-args': 7
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
